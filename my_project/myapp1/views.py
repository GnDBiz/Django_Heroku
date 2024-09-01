from typing import Any
from django.shortcuts import render
#Templatesファイルを結び付ける
from django.views.generic import TemplateView

#関数を作成
#index.htmlを表示
class IndexView(TemplateView):
    #Templatesファイルのindex.htmlを追加
    template_name = "index.html"

    #コンテキストデータを記述
    # HTMLに渡したい変数を定義できる場所(index.html内のみで適応)
    def get_context_data(self):
        ctxt = super().get_context_data()
        #変数に定義したい文字を代入し紐づける。(ユーザ名)
        ctxt["username"] = "太郎"
        return ctxt
                         
#about.htmlを表示
class aboutpage(TemplateView):
    #Templatesファイルのindex.htmlを追加
    template_name = "about.html"

    #コンテキストデータを記述
    # HTMLに渡したい変数を定義できる場所(index.html内のみで適応)
    def get_context_data(self):
        ctxt = super().get_context_data()
        #変数に定義したい文字を代入し紐づける。(今まで作成したサービスの個数)
        ctxt["num_services"] = 12345678
        #変数に定義したい文字を代入し紐づける。(習得したスキルのリスト)
        #記述方法は普通のpythonの書き方
        ctxt["skills"] = [
             "・Python",
             "・C++",
             "・Javascript",
             "・Rust",
             "・Go",
        ]
        return ctxt

# Create your views here.
