#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

#login:user:自分のアカウント名
#passward:自分のパスワード
#like_per_day:1日にいいねする数
#comments_per_day:1日にコメントする数
#tag_list:いいねするハッシュタグリスト
#tag_blacklist:入っていたら、いいねしないハッシュタグリスト
#max_like_for_one_tag:１つのタグに対して最大どのくらいいいねするか
#follow_per_day:1日にフォローする数
#unfollow_per_day:1日にアンフォローする数
#unfollow_break_min:最小でどのくらいフォロワーを減らすか
#unfollow_break_max:最大でどのくらいフォロワーを減らすか
#log_mod:0=コンソールにログを表示　1=ファイルにログを残す　2=ログ残さない

bot = InstaBot(
    login="ryosuke_katano",
    password="19910124",
    like_per_day=5000,
    comments_per_day=0,
    tag_list=['ゴルフ', 'ドラム', '飯テロ', 'ギター', 'バンド'],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=5,
    tag_blacklist=[],
    user_blacklist={},
    follow_per_day=0,
    follow_time=0 * 60,
    unfollow_per_day=0,
    unfollow_break_min=0,
    unfollow_break_max=0,

"""
The example.py is deprecated. Please use the declarative mode with YAML settings
Please refer to Github README + (instabot -h) + Blog section for further information
"""
print(__doc__)