# Trial Search 

## 1 Overview

The project Trial Search mainly consists of a spider that scrapes the [jrct website](https://jrct.niph.go.jp/B) and stores the data in mysql database.

In this article, we will list and explain some core commands related to the launch and execution of spider, with a detailed example.

## 2 Directory Structure

    ├─pyenv
    │  └─src
    │      └─trial_search_crawler
    │          └─trial_search_crawler
    │              ├─spiders
    │              └─utils
    └─sqlenv
        └─mysql
            ├─db
            │  ├─#innodb_redo
            │  ├─#innodb_temp
            │  ├─jrctdb
            │  ├─mysql
            │  ├─performance_schema
            │  ├─sys
            │  └─testdb
            └─initdb.d
