#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:46:01 2018

@author: Bandar Almohsen, Mengxi Shen
"""
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("users.tsv",delimiter="\t")
df2 = pd.read_csv("messages.tsv",delimiter="\t")
df3 = pd.read_csv("discussions.tsv",delimiter="\t")
df4 = pd.read_csv("discussion_posts.tsv",delimiter="\t")
# total users
total_user=(df1["id"].shape)[0]
print(total_user)
df5 = pd.merge(df1,df2,how="right", on="id")
df6 = pd.merge(df5,df3,how="left", on="id")
data1 = pd.merge(df6,df4,how="left", on="id")
# time span
dmax=data1.max()
time_max=dmax[["memberSince","createDate_x","createDate_y","sendDate"]].max()
time_min=(data1[["memberSince","createDate_x","createDate_y","sendDate"]].min(axis=0)).min()
time_span=(time_max-time_min)/(24*60*60*1000)# convert milliseconds to days(24hr)
# pie chart for messages 
mcounts=data1["type"].value_counts().to_dict()
mname=mcounts.keys()
mnum=mcounts.values()
plt.figure(1,figsize=(15,15))
plt.pie(x=mnum, labels=mname,autopct='%1.1f%%')
plt.savefig("message_type.png")
# pie chart for discussions
plt.figure(2,figsize=(15,15))
dcounts=data1["discussionCategory"].value_counts().to_dict()
dname=dcounts.keys()
dnum=dcounts.values()
plt.pie(x=dnum,labels=dname,autopct='%1.1f%%')
plt.savefig("decission_type.png")
# the number of discussions have been posted already
havepos=data1["discussion_id"].unique()
print((havepos.shape)[0])
# distribution histogram of activity time range 
gdf1=data1.groupby("sender_id")["sendDate"].agg(["max","min"])
mesrange=(gdf1["max"]-gdf1["min"])/(24*60*60*1000)
plt.figure(3,figsize=(15,15))
plt.hist(mesrange,log=True)
plt.xlabel("days")
plt.ylabel("amount_of_users")
plt.savefig("activity_range.png")
# message activity delay in each category
data2=(pd.merge(df1,df2,left_on="id",right_on="sender_id")).groupby("id_x")
early_d=data2.min()
FLR=early_d.loc[early_d["type"] == "FRIEND_LINK_REQUEST"]
FLR_actdely=(FLR["sendDate"]-FLR["memberSince"])/(24*60*60*1000)
DM=early_d.loc[early_d["type"] == "DIRECT_MESSAGE"]
DM_actdely=(DM["sendDate"]-DM["memberSince"])/(24*60*60*1000)
plt.figure(4, figsize=(15,15))
plt.hist(FLR_actdely,log=True,alpha=0.5,label="Friend Link Request")
plt.hist(DM_actdely,log=True,alpha=0.5,label="Direct Message")
plt.legend(loc="upper right")
plt.xlabel("days")
plt.ylabel("amount_of_users")
plt.savefig("message_activity_delay.png")
# distribution of discussion categories by the number of posts
data3=pd.merge(df3,df4,left_on="id",right_on="discussion_id")
cate_counts=data3["discussionCategory"].value_counts().to_dict()
xvalue=cate_counts.values()
lvalue=cate_counts.keys()
plt.figure(5,figsize=(15,15))
plt.pie(x=xvalue,labels=lvalue,autopct='%1.1f%%',explode=(0.1,0,0,0,0,0,0,0,0))
plt.savefig("discussion_categories_distribution.png")
# post activity delay
data4=(pd.merge(df1,df4,left_on="id",right_on="creator_id")).groupby("creator_id")
early_data=data4.min()
post_delay=(early_data["createDate"]-early_data["memberSince"])/(24*60*60*1000)
plt.figure(6,figsize=(15,15))
plt.hist(post_delay,log=True)
plt.xlabel("days")
plt.ylabel("amount_of_users")
plt.savefig("post_delay.png")
# box plot with whiskers
plt.figure(7,figsize=(15,15))
plt.subplot(1, 4, 1)
plt.title("Friend Request")
plt.boxplot(FLR_actdely)
plt.yscale('log')
plt.subplot(1, 4, 2)
plt.title("Direct message")
plt.boxplot(DM_actdely)
plt.yscale('log')
plt.subplot(1, 4, 3)
plt.title("Post Activity")
plt.boxplot(post_delay)
plt.yscale('log')
plt.subplot(1, 4, 4)
plt.title("Activity")
plt.boxplot(mesrange)
plt.yscale('log')
plt.savefig("box_plot.png")
