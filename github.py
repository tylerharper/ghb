#!/usr/bin/env python
import snooze
import json
import sys
import subprocess
import os
import pystache
from ficcle import Ficcle

user = subprocess.Popen(["git", "config", "--global", "github.user"], stdout=subprocess.PIPE).stdout.read().strip('\n ') 
token = subprocess.Popen(["git", "config", "--global", "github.token"], stdout=subprocess.PIPE).stdout.read().strip('\n ') 

github = snooze.Snooze('github.com/api/v2/json', secure=True)

def display_info(info):
    for x in info:
        for y in x:
            print '%s: %s' % (str(y), str(x[y]))

def display_user(info):
    for x in info:
        print '%s: %s' % (str(x), str(info[x]))

def edit(option, arg):
    resp = github.user.show.username[user](_method_='post', values={option: arg}, login=user, token=token)
    resp_python = json.loads(resp)
    display_user(resp_python['user'])

def show(arg):
    resp = github.user.show.username[arg](_method_='get')
    resp_python = json.loads(resp)
    display_user(resp_python['user'])

def create(name, description=None, homepage=None, public=1):
    args = {'name': name, 'public':public, 'login':user, 'token' : token}
    if description != None:
        args['description'] = description
    if homepage != None:
        args['homepage'] = homepage

    resp = github.repos.create(_method_='post', **args)
    print resp

def delete(name, delete_token=None):
    resp = github.repos.delete.repo[name](_method_='post', delete_token=delete_token, login=user, token=token)
    
    del_token = json.loads(resp)['delete_token']
    
    print 'If you are sure you want to delete repository %s call:' % name
    print '%s %s %s' % (sys.argv[0], sys.argv[1], del_token)

def issue_list(repo, username=user, state='open'):
    resp = github.issues.list.user[user].repo[repo].state[state](_method_ = 'get')
    issues = json.loads(resp)
    v = pystache.View(context=issues)
    v.template_name = 'templates/issue-list'
    print v.render()
    
def repo_search(search):
    resp = github.repos.search.search_str[search](_method_='get')
    results = json.loads(resp)
    v = pystache.View(context=results)
    v.template_name = 'templates/repo-search'
    print v.render() 
 
def user_repos(username=user):
    resp = github.repos.show.user[username](_method_='get')
    results = json.loads(resp)
    v = pystache.View(context=results)
    v.template_name = 'templates/user-repos'
    print v.render() 
    
def show_repo(repo, username=user):
    resp = github.repos.show.user[username].repo[repo](_method_='get')
    results = json.loads(resp)
    results['repository'] = [results['repository']] # used for pystache
    v = pystache.View(context=results)
    v.template_name = 'templates/show-repo'
    print v.render()

if __name__ == '__main__':
    fickle = Ficcle()

    fickle.add_function(edit)
    fickle.add_function(show)
    fickle.add_function(create)
    fickle.add_function(delete)
    fickle.add_function(issue_list, name='issue-list')
    fickle.add_function(repo_search, name='search-repo')
    fickle.add_function(user_repos, name='user-repos')
    fickle.add_function(show_repo, name='show-repo')

    fickle.run_ficcle()

