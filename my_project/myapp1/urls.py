from django.urls import path

#同じデレクトリ階層のviews関数ファイルをインポート
from .views import IndexView,aboutpage

#URLの定義
urlpatterns = [
    #''はトップページであることを表している。
    #パスでもし一番最初の’’URLに移動したらIndexView(index.htmlファイルを表示させるクラス)を処理するように指定
    path('', IndexView.as_view()),
    #パスでもし'about/'に飛んだらtestpageに行くように表示
    path('about/', aboutpage.as_view()),
]