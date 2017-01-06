---
title: Burp Suite使用介绍（一）
date: 2017-01-06 10:30:09
tags: burpsuit
categories: 工具使用
---

##Getting Started##
Burp Suite 是用于攻击web 应用程序的集成平台。它包含了许多工具，并为这些工具设计了许多接口，以促进加快攻击应用程序的过程。所有的工具都共享一个能处理并显示HTTP 消息，持久性，认证，代理，日志，警报的一个强大的可扩展的框架。本文主要介绍它的以下特点：

- **Target(目标)**
显示目标目录结构的的一个功能

- **Proxy(代理)**
拦截HTTP/S的代理服务器，作为一个在浏览器和目标应用程序之间的中间人，允许你拦截，查看，修改在两个方向上的原始数据流。

- **Spider(蜘蛛)**
应用智能感应的网络爬虫，它能完整的枚举应用程序的内容和功能。

- **Scanner(扫描器)**
高级工具，执行后，它能自动地发现web 应用程序的安全漏洞。

- **Intruder(入侵)**
一个定制的高度可配置的工具，对web应用程序进行自动化攻击，如：枚举标识符，收集有用的数据，以及使用fuzzing 技术探测常规漏洞。

- **Repeater(中继器)**
一个靠手动操作来触发单独的HTTP 请求，并分析应用程序响应的工具。

- **Sequencer(会话)**
用来分析那些不可预知的应用程序会话令牌和重要数据项的随机性的工具。

- **Decoder(解码器)**
进行手动执行或对应用程序数据者智能解码编码的工具。

- **Comparer(对比)**
通常是通过一些相关的请求和响应得到两项数据的一个可视化的“差异”。

- **Extender(扩展)**
可以让你加载Burp Suite的扩展，使用你自己的或第三方代码来扩展Burp Suit的功能。

- **Options(设置)**
对Burp Suite的一些设置

###测试工作流程
Burp支持手动的Web应用程序测试的活动。它可以让你有效地结合手动和自动化技术，使您可以完全控制所有的BurpSuite执行的行动，并提供有关您所测试的应用程序的详细信息和分析。 让我们一起来看看Burp Suite的测试流程过程吧。 如下图
![](https://lyxw.github.io/assets/img/articles/burp1.png)
###简要分析
代理工具可以说是Burp Suite测试流程的一个心脏，它可以让你通过浏览器来浏览应用程序来捕获所有相关信息，并让您轻松地开始进一步行动，在一个典型的测试中，侦察和分析阶段包括以下任务：

- **手动映射应用程序**
使用浏览器通过BurpSuite代理工作，手动映射应用程序通过以下链接，提交表单，并通过多步骤的过程加强。这个过程将填充代理的历史和目标站点地图与所有请求的内容，通过被动蜘蛛将添加到站点地图，可以从应用程序的响应来推断任何进一步的内容(通过链接、表单等)。也可以请求任何未经请求的站点(在站点地图中以灰色显示的)，并使用浏览器请求这些。

- **在必要是执行自动映射**
您可以使用BurpSuite自动映射过程中的各种方法。可以进行自动蜘蛛爬行，要求在站点地图未经请求的站点。请务必在使用这个工具之前，检查所有的蜘蛛爬行设置。
使用内容查找功能发现，可以让您浏览或蜘蛛爬行可见的内容链接以进一步的操作。
使用BurpSuite Intruder(入侵者)通过共同文件和目录列表执行自定义的发现，循环，并确定命中。
注意，在执行任何自动操作之前，可能有必要更新的BurpSuite的配置的各个方面，诸如目标的范围和会话处理。

- **分析应用程序的攻击面**
映射应用程序的过程中填入代理服务器的历史和目标站点地图与所有的BurpSuite已抓获有关应用程序的信息。这两个库中包含的功能来帮助您分析它们所包含的信息，并评估受攻击面的应用程序公开。此外，您可以使用BurpSuite的目标分析器报告的攻击面的程度和不同类型的应用程序使用的URL 。
接下来主要介绍下BurpSuite的各个功能吧。先介绍Proxy功能，因为Proxy起到一个心脏功能，所有的应用都基于Proxy的代理功能。

###Burp Suite功能按钮键翻译对照
| 导航栏                         |                  |                                        |                          |
|:------------------------------ | :--------------- | :------------------------------------- | :----------------------- |
| Burp 	                         | BurpSuite 	    | save state wizard 	                 | 保存状态向导             |
| restore state                  | 恢复状态 	    | Remember setting 	                     | 记住设置                 |
| restore defaults 	             | 恢复默认 	    | Intruder 	                             | 入侵者                   |
| Start attack 	                 | 开始攻击(爆破)   | Actively scan defined insertion points | 定义主动扫描插入点       |
| Repeater 	                     | 中继器 	        | New tab behavior 	                     | 新标签的行为             |
| Automatic payload positions    | 自动负载位置     | config predefined payload lists 	     | 配置预定义的有效载荷清单 |
| Update content-length 	     | 更新内容长度     | unpack gzip/deflate 	                 | 解压gzip/放弃            |
| Follow redirections 	         | 跟随重定向 	    | process cookies in redirections 	     | 在重定向过程中的cookies  |
| View 	                         | 视图 	        | Action 	                             | 行为                     |

| 功能项                         |                  |                                        |                          |
|:------------------------------ | :--------------- | :------------------------------------- | :----------------------- | 	  	  
| Target 	                     | 目标 	        | Proxy 	                             | 代理                     |
| Spider 	                     | 蜘蛛 	        | Scanner 	                             | 扫描                     |
| Intruder 	                     | 入侵者 	        | Repeater 	                             | 中继器                   |
| Sequencer 	                 | 定序器 	        | Decoder 	                             | 解码器                   |
| Comparer 	                     | 比较器 	        | Extender 	                             | 扩展                     |
| Options 	                     | 设置 	        | Detach 	                             | 分离                     |
| Filter 	                     | 过滤器 	        | SiteMap 	                             | 网站地图                 |
| Scope 	                     | 范围 	        | Filter by request type 	             | 通过请求过滤             |
| Intercept 	                 | 拦截 	        | response Modification 	             | 响应修改                 |
| match and replace 	         | 匹配和替换 	    | ssl pass through 	                     | SSL通过                  |
| Miscellaneous 	             | 杂项 	        | spider status 	                     | 蜘蛛状态                 |
| crawler settings 	             | 履带式设置 	    | passive spidering 	                 | 被动蜘蛛                 |
| form submission 	             | 表单提交 	    | application login 	                 | 应用程序登录             |
| spider engine 	             | 蜘蛛引擎 	    | scan queue 	                         | 扫描队列                 |
| live scanning 	             | 现场扫描 	    | live active scanning 	                 | 现场主动扫描             |
| live passive scanning 	     | 现场被动扫描 	| attack insertion points 	             | 攻击插入点               |
| active scanning optimization   | 主动扫描优化 	| active scanning areas 	             | 主动扫描区域             |
| passive scanning areas 	     | 被动扫描区域 	| Payload 	                             | 有效载荷                 |
| payload processing 	         | 有效载荷处理 	| select live capture request 	         | 选择现场捕获请求         | 
| token location within response | 内响应令牌的位置 | live capture options 	                 | 实时捕捉选项             |
| Manual load 	                 | 手动加载 	    | Analyze now 	                         | 现在分析                 |
| Platform authentication 	     | 平台认证 	    | Upstream proxy servers 	             | 上游代理服务器           |
| Grep Extrack 	                 | 提取             |                                        |                          |	  	  
##Proxy功能##
Burp Proxy相当于BurpSuite的心脏，通过拦截，查看和修改所有的请求和响应您的浏览器与目标Web服务器之间传递。 下面了解有关BurpProxy：
![](https://lyxw.github.io/assets/img/articles/burp2.png)
###Using BurpProxy http、https
**http**
设置代理的方法：以http ie为例：
`工具>>Internet选项>>连接>>局域网>>勾选代理服务器填写地址127.0.0.1端口8080`
这里端口可以随便定义但是要跟burp的监听端口要一致然后保存再到Proxy的Options中添加add
![](https://lyxw.github.io/assets/img/articles/burp3.png)
![](https://lyxw.github.io/assets/img/articles/burp4.png)
这样http协议的监听就可以了,当intercept is on表示开启拦截功能，反之
![](https://lyxw.github.io/assets/img/articles/burp5.png)
这样就代表拦截成功，我们可以右击send to Repeater去修改数据再发送，也可以右击改变提交请求方式(change request method)比如get或者post等功能。

**https**
`1.以管理员权限运行ie浏览器`
`2.像http那样配置好代理`
`3.在地址栏访问https地址，单击继续` 
`4.点击错误证书在这个地址栏` 
`5.点击查看证书` 
`6.在证书路径选项卡点击PortSwigger CA,然后再点击查看证书` 
`7.在常规选项卡里点击安装证书` 
`8.在证书导入向导中，选择“将所有的证书放入下列存储区”` 
`9.点击浏览` 
`10.以当前用户或者本机计算机都可以` 
`11.点击ok完成导入` 
`12.重启ie（不需要以管理员权限运行）` 
其它浏览器差不多具体请查看官网http://portswigger.net/burp/Help/proxy_options_installingCAcert.html

**Intercept**
用于显示和修改HTTP请求和响应，通过你的浏览器和Web服务器之间。在BurpProxy的选项中，您可以配置拦截规则来确定请求是什么和响应被拦截(例如，范围内的项目，与特定文件扩展名，项目要求与参数，等)。 该面板还包含以下控制：
- **Forward**
当你编辑信息之后，发送信息到服务器或浏览器

- **Drop**
当你不想要发送这次信息可以点击drop放弃这个拦截信息

- **Interception is on/off**
这个按钮用来切换和关闭所有拦截。如果按钮显示Interception is On，表示请求和响应将被拦截或自动转发根据配置的拦截规则配置代理选项。如果按钮显示Interception is off则显示拦截之后的所有信息将自动转发。

- **Action**
说明一个菜单可用的动作行为操作可以有哪些操作功能。

- **Comment field**
为请求或响应添加注释，以便更容易在History选项卡中识别它们。

- **Highlight**
为请求或响应添加颜色，可以在history选项卡和截获中更容易发现。

- **History**
代理历史认为每个请求和响应。通过代理可以记录全部请求和响应。您可以过滤和注释这个信息来帮助管理它，并使用代理的历史来测试流程。History(代理历史)总在更新，即使你把Interception turned off(拦截关闭)，允许浏览不中断的同时还监测应用流量的关键细节。

- **History Table**
表中显示已通过代理HTTP消息的所有请求，并且可以查看完整的你所做的任何修改和截获的信息的请求和响应。 表中包含以下字段：
```
# (请求索引号)、Host(主机)、Method(请求方式)、URL(请求地址)、Params(参数)、Edited(编辑)、Status(状态)、Length(响应字节长度)、MIME type(响应的MLME类型)、Extension(地址文件扩展名)、Title(页面标题)、Comment(注释)、SSL、IP(目标IP地址)、Cookies、Time(发出请求时间)、Listener port(监听端口)。
```
![](https://lyxw.github.io/assets/img/articles/burp6.png)
您可以通过单击任何列标题进行升序或降序排列。如果您在表中双击选择一个项目地址，会显示出一个详细的请求和响应的窗口。或者右击选择`Show new history window`
![](https://lyxw.github.io/assets/img/articles/burp7.png)

**Display Filter**
Proxy histroy有一个可以用来在视图中隐藏某些内容的功能，以使其更易于分析和你感兴趣的工作内容的显示过滤。 History Table上方的过滤栏描述了当前的显示过滤器。点击过滤器栏打开要编辑的过滤器选项。该过滤器可以基于以下属性进行配置：
![](https://lyxw.github.io/assets/img/articles/burp8.png)
- **Request type**
Show only in-scope items--勾选则显示在范围内的项目，反之。

- **MIME type**
您可以设定是否显示或隐藏包含各种不同的MIME类型，如HTML，CSS或图像的响应。

- **Status code**
您可以设定是否要显示或隐藏各种HTTP状态码响应。

- **Search term**
您可以过滤对反应是否不包含指定的搜索词。您可以设定搜索词是否是一个文字字符串或正则表达式，以及是否区分大小写。如果您选择了“Negative search (消极搜索)”选项，然后不匹配的搜索词唯一的项目将被显示。

- **File extension**
您可以设定是否要显示或隐藏指定的文件扩展名的项目。

- **Annotation**
您可以设定是否显示使用用户提供的评论或仅亮点项目。

- **Listener**
你可以只显示特定的监听端口上接收的项目。测试访问控制时可能有用。 如果设置一个过滤器，隐藏一些项目，这些都没有被删除，只是隐藏起来，如果你取消设置相关的过滤器将再次出现。这意味着您可以使用筛选器来帮助您系统地研究了大量代理的历史来理解各种不同的请求显示。

**Annotations**
您可以通过添加注释和批注亮点代理历史记录项。这可能是有用的描述不同要求的目的，并标记了进一步查看。 两种方式添加亮点： 1)使用在最左边的表列中的下拉菜单中突出显示单个项目。 2)可以突出显示使用上下文菜单中的“亮点”项目的一个或多个选定的项目。 两种方法添加注释： 1)双击相关条目，注释列中，添加或编辑就地评论。 2)发表评论使用上下文菜单中的“添加注释”项目的一个或多个选定的项目。 除了以上两种，您也可以注释项目，它们出现在拦截选项卡，这些都将自动出现在历史记录表。 当您已经注明想要的请求，您可以使用列排序和显示过滤器后迅速找到这些项目。

**Options**
设置代理监听、请求和响应，拦截反应，匹配和替换，ssl等。

**Proxy Listeners**
代理侦听器是侦听从您的浏览器传入的连接本地HTTP代理服务器。它允许您监视和拦截所有的请求和响应，并且位于BurpProxy的工作流的心脏。默认情况下，Burp默认监听12.0.0.1地址，端口8080。要使用这个监听器，你需要配置你的浏览器使用127.0.0.1:8080作为代理服务器。此默认监听器是必需的测试几乎所有的基于浏览器的所有Web应用程序。
![](https://lyxw.github.io/assets/img/articles/burp9.png)

- **Binding**
这些设置控制Burp怎么代理监听器绑定到本地网络接口：
```
Bind to port---这是将被打开侦听传入连接的本地接口上的端口。你将需要使用一个没有被绑定被其他应用程序的闲置端口。
Bind to address---这是Burp绑定到本地接口的IP地址。
```
您可以绑定到刚刚127.0.0.1接口或所有接口，或任何特定的本地IP地址。
注意：如果监听器绑定到所有接口或特定的非loopback接口，那么其他计算机可能无法连接到该侦听器。这可能使他们发起出站连接，从您的IP地址发起，并以访问代理服务器历史的内容，其中可能包含敏感数据，如登录凭据。你应该只启用此当你位于一个受信任的网络上。
BurpSuite让您创建多个代理服务器的侦听器，并提供了丰富的控制自己的行为的配置选项。你可能偶尔需要进行测试时不寻常的应用，或与一些非基于浏览器的HTTP客户端进行合作，利用这些选项。

- **Request Handling**
这些设置包括选项来控制是否BurpSuite重定向通过此侦听器接收到的请求：
**Redirect to host** - 如果配置了这个选项，Burp会在每次请求转发到指定的主机，而不必受限于浏览器所请求的目标。需要注意的是，如果你正使用该选项，则可能需要配置匹配/替换规则重写的主机头中的请求，如果服务器中，您重定向请求预期，不同于由浏览器发送一个主机头。
**Redirect to port** - 如果配置了这个选项，Burp会在每次请求转发到指定的端口，而不必受限于浏览器所请求的目标。
**Force use of SSL** - 如果配置了这个选项，Burp会使用HTTPS在所有向外的连接，即使传入的请求中使用普通的HTTP。您可以使用此选项，在与SSL相关的响应修改选项结合，开展sslstrip般的攻击使用Burp，其中，强制执行HTTPS的应用程序可以降级为普通的HTTP的受害用户的流量在不知不觉中通过BurpProxy代理。
注意：每一个重定向选项都可以单独使用。因此，例如，可以将所有请求重定向到一个特定的主机，同时保留原来的端口和协议在每个原始请求中使用。隐形BurpProxy的支持允许非代理感知客户端直接连接到监听。

- **Certificate**
这些设置控制呈现给客户端的SSL服务器的SSL证书。使用这些选项可以解决一些使用拦截代理时出现的SSL问题：
```
你可以消除您的浏览器的SSL警报，并需要建立SSL例外。 
凡网页加载来自其他域的SSL保护的项目，您可以确保这些均可由浏览器加载，而不需要先手动接受每个引用的域代理的SSL证书。 
您可以与拒绝连接到服务器，如果接收到无效的SSL证书胖客户端应用程序的工作。 
```
下列选项可用：
**Use a self-signed certificate** 一个简单的自签名SSL证书提交给您的浏览器，它总是导致SSL警告。
**Generate CA-signed per-host certificate** 这是默认选项。安装后，BurpSuite创造了一个独特的自签名的证书颁发机构（CA）证书，并将此计算机上使用，每次BurpSuite运行。当你的浏览器发出SSL连接到指定的主机，Burp产生该主机，通过CA证书签名的SSL证书。您可以安装BurpSuite的CA证书作为在浏览器中受信任的根，从而使每个主机的证书被接受，没有任何警报。您还可以导出其他工具或Burp的其他实例使用CA证书。
**Generate a CA-signed certificate with a specific hostname** 这类似于前面的选项;然而，Burp会产生一个单一的主机证书与每一个SSL连接使用，使用您指定的主机名。在进行无形的代理时，此选项有时是必要的，因为客户端没有发送连接请求，因此Burp不能确定SSL协议所需的主机名。你也可以安装BurpSuite的CA证书作为受信任的根。
**Use a custom certificate** 此选项使您可以加载一个特定的证书（在PKCS＃12格式）呈现给你的浏览器。如果应用程序使用它需要特定的服务器证书（例如一个给定序列号或证书链）的客户端应该使用这个选项。

- **Exporting and Importing the CA Certificate**
您可以导出您安装特定的CA证书在其他工具或BurpSuite的其他情况下使用，并且可以导入证书Burp在当前实例使用。 您可以选择要导出的证书只（用于导入到您的浏览器或其他设备的信任），或者你可以同时导出的证书及其私钥。
注意：您不应该透露的私钥证书给任何不可信的一方。拥有你的证书和密钥的恶意攻击者可能可以，即使你不使用Burp拦截浏览器的HTTPS流量。
您也可以仅通过访问http://burp/cert在浏览器中导出证书。它使HTTPS请求您的浏览器相同的证书，但在一些移动设备上安装时，设备通过一个URL来下载它是有帮助的。
