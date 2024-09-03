# Oncolo JRCT Crawler

## 1 Overview

The project Trial Search mainly consists of a spider that scrapes the [jrct website](https://jrct.niph.go.jp/B) and stores the data in mysql database.

In this article, we will list and explain some core commands related to the launch and execution of spider, with a detailed example.

## 2 Directory Structure

.
├── README.md
├── app
│   └── src
│       └── main.py
└── docker
    ├── docker-compose.yml
    ├── mysql
    │   ├── Dockerfile
    │   ├── initdb.d
    │   │   └── init.sql
    │   └── my.cnf
    └── scrapy
        ├── Dockerfile
        └── requirements.txt
