# Chapter 14: Securities Markets: Taking Orders and Executing Trades
# 第 14 章：证券市场：接受订单与执行交易

Part of your function as a registered rep will be to understand and explain to customers (and potential customers) how the stock market works. I designed this chapter with that in mind (along with the fact that you need to know this stuff for the SIE, of course).
作为一名登记代表，您的部分职责是理解并向客户（及潜在客户）解释股票市场是如何运作的。我设计本章时正是基于这一考量（当然，这也是因为您需要掌握这些内容以应对 SIE 考试）。

In this chapter, I cover the basics of exchanges and the over-the-counter (OTC) market, along with some of the active participants who help the market run smoothly (at least most of the time). Pay particular attention to the sections “Reviewing basic order types” and “Factoring in order features,” because you’ll definitely use that information every day after you pass the SIE and corequisite tests.
在本章中，我将涵盖交易所和场外交易 （OTC） 市场的基本知识，以及一些帮助市场平稳运行（至少大部分时间是这样）的活跃参与者。请特别关注“回顾基本订单类型”和“考虑订单特征”这两节，因为在您通过 SIE 及相关进阶考试后，您每天都会用到这些信息。

---

## 1. Shopping at Primary and Secondary Markets
## 1. 在一级市场与二级市场购物

Depending on whether the securities are new or outstanding, they trade in either the primary or secondary market.
根据证券是新发行的还是已流通的，它们分别在一级市场或二级市场进行交易。

### Buying new in the primary market
### 在一级市场购买新股

The **primary market** (new issue market) is where the issuer receives the proceeds from the sale of securities. A security that has never been offered or sold to the public is considered a new issue. Here are the three types of offerings on the primary market:
**一级市场 （Primary market）**（新发行市场）是发行人获取证券销售收入的市场。从未向公众提供或出售过的证券被视为新发行证券。以下是一级市场的三种发行类型：

*   **Initial public offering (IPO)**: An IPO is the first time a corporation ever sells stock to the public to raise capital. When a corporation is in the process of issuing securities for the first time, it’s said to be **going public**.
*   **首次公开募股 （IPO）**：IPO 是公司第一次向公众出售股票以筹集资金。当公司第一次发行证券时，就被称为**上市 （going public）**。
*   **Primary offering**: A primary offering is the issuer market, where the issuer is selling shares to raise money. Certainly, an IPO falls into that category. However, the corporation usually holds shares back for future use; it later pulls those securities out of storage and sells them in a **subsequent** (add-on, additional, or follow-up) offering, which is also a primary offering.
*   **一级发行 （Primary offering）**：一级发行是发行人市场，即发行人通过出售股份来筹集资金。IPO 当然属于这一类。然而，公司通常会保留一部分股份供未来使用；之后再将这些证券从“储藏室”中取出，并在**后续**（增发、追加或随后的）发行中出售，这同样属于一级发行。
*   **Combined (split) offering**: This type of offering is a combination of new securities and a large block of outstanding or previously outstanding securities.
*   **组合（混合）发行 （Combined/split offering）**：这种发行类型是新证券与大笔已流通（或之前已流通）证券的结合。

🧠 **REMEMBER**
When securities are sold in the primary market, the **bulk of the sales proceeds goes to the issuer** and the balance goes to the entity or entities responsible for selling the securities to the public — the underwriter(s) and selling group members (if any).
🧠 **请记住**
当证券在一级市场出售时，**销售收益的大部分归发行人所有**，余额则归负责向公众销售证券的实体——即承销商和销售小组成员（如果有的话）。

### Buying used in the secondary market
### 在二级市场购买“二手”股

When the securities are already trading in the market, the sales proceeds go to **another investor** instead of to the issuer. The secondary market, also called the **aftermarket**, consists of the following categories:
当证券已经在市场上交易时，销售收益流向**另一名投资者**，而不是发行人。二级市场（也称为**后续市场 aftermarket**）由以下类别组成：

*   **First market**： Trading of **listed securities** on an exchange floor （e。g。， NYSE）。 （第一市场：在交易所大厅交易的**上市证券**。）
*   **Second market**： Trading of **unlisted securities** over-the-counter （OTC）。 （第二市场：场外交易的**非上市证券**。）
*   **Third market**： The trading of **exchange-listed securities** in the over-the-counter （OTC） market。 （第三市场：在场外交易 （OTC） 市场交易的**交易所上市证券**。）
*   **Fourth market**： The trading of securities **between institutions** without the use of a brokerage firm。 These trades are typically executed through **electronic communication networks （ECNs）** such as Instinet。 （第四市场：**机构之间**不通过经纪公司而直接进行的证券交易。这些交易通常通过 Instinet 等**电子通信网络 （ECNs）** 执行。）

💡 **TIP**
You’re more likely to get a question on the third or fourth market than the first or second.
💡 **提示**
在考试中，您遇到关于第三或第四市场的问题的可能性比第一或第二市场要大。

---

## 2. Making the Trade
## 2. 执行交易

After securities are issued publicly, they may trade on an exchange or on the OTC market.
证券公开发行后，可以在交易所或场外交易 （OTC） 市场进行交易。

### Auctioning securities at securities exchanges
### 在证券交易所拍卖证券

Exchanges are **auction markets**, where bidders and sellers get together to execute trades.
交易所是**拍卖市场**，买卖双方聚集在一起执行交易。

*   All exchanges have a **trading floor**。 （所有交易所都有一个交易大厅。）
*   Each security listed on an exchange has its own **trading post** （location） on the floor。 （在交易所上市的每种证券在大厅都有自己的交易点。）
*   **Designated market makers （DMMs）** （formerly specialists）： These professionals manage the auction market for a particular security。 Their purpose is to maintain a **“fair and orderly market。”** A DMM can act as a broker or a dealer。 An important function of a DMM is to keep track of and execute **limit orders**。 （**指定做市商 （DMMs）**（原名特种商）：这些专业人士管理特定证券的拍卖市场。他们的目的是维持**“公平且有序的市场”**。DMM 既可以作为经纪人，也可以作为自营商。DMM 的一个重要功能是记录并执行**限价单**。）

### Negotiating trades over the counter
### 在场外协商交易

Unlike exchanges, the OTC market is considered a **negotiated market**. Instead of yelling out prices, traders buy and sell by way of telephone or computer transactions.
与交易所不同，场外交易 （OTC） 市场被视为**协商市场**。交易者不是大声喊价，而是通过电话或计算机交易来买卖证券。

*   **OTCBB （Over the Counter Bulletin Board）**： A quotation service operated by FINRA for unlisted （non-Nasdaq） securities。 （OTCBB：由 FINRA 运营的为非上市（非纳斯达克）证券提供的报价服务。）
*   **Pink Market （Pink Sheets）**： For corporations too small to be placed on the OTCBB。 They are not required to meet listing requirements or file with the SEC。 （**粉单市场**：适用于规模太小而无法在 OTCBB 上市的公司。他们不需要满足上市要求或向 SEC 备案。）

🧠 **REMEMBER**
**U.S. government and municipal bonds trade only OTC.**
🧠 **请记住**
**美国政府债券和市政债券仅在场外交易 （OTC） 交易。**

---

## 3. Understanding the Role of a Broker-Dealer
## 3. 理解经纪自营商的角色

For a firm to be considered a **broker-dealer**, it must buy and sell securities from its own account and act as a middleman for securities not in inventory.
对于一家被称为**经纪自营商 （broker-dealer）** 的公司，它必须既能利用自有账户买卖证券，又能为不在库存中的证券充当中间人。

*   **Broker （Agent）**： A firm is acting as a broker when it **doesn't use its own inventory**。 A broker charges a **commission**。 The terms *broker* and *agent* may be used interchangeably。 （经纪人（代理人）：当公司**不使用自有库存**时，它是在作为经纪人行事。经纪人收取**佣金**。术语“经纪人”和“代理人”可以互换使用。）
*   **Dealer （Principal）**： A firm is acting as a dealer when it **uses its own inventory**。 A dealer charges a **markup** （when selling） or a **markdown** （when buying）。 The terms *dealer*， *principal*， and *market maker* may be used interchangeably。 （自营商（主事人）：当公司**使用自有库存**时，它是在作为自营商行事。自营商收取**加价 （markup）**（卖出时）或**减价 （markdown）**（买入时）。术语“自营商”、“主事人”和“做做市商”可以互换使用。）

🧠 **REMEMBER**
A firm **can't act as a broker and a dealer for the same trade**. Charging a markup and a commission on the same trade is a violation.
🧠 **请记住**
公司**不能在同一笔交易中同时充当经纪人和自营商**。在同一笔交易中同时收取加价和佣金是违规行为。

---

## 4. Receiving and Executing Customer Orders
## 4. 接收并执行客户订单

🧠 **REMEMBER**
**Unlicensed associated persons** cannot receive or execute orders for customers. In order to discuss investment objectives or take orders, the person must be **licensed**.
🧠 **请记住**
**未经许可的关联人员**不能接收或执行客户订单。为了讨论投资目标或接受订单，该人员必须**持有执照**。

### Reviewing basic order types
### 回顾基本订单类型

*   **Market order**： For immediate execution at the **best price available**。 （市价单：按**当前最优价格**立即执行。）
*   **Selling short**： Selling securities they don't actually own （borrowed from a lender）。 A short seller is **bearish**。 All short sales must be executed in **margin accounts**。 （卖空：卖出并不实际拥有的证券（从借出人处借入）。卖空者是**看空**的。所有卖空交易必须在**融资账户**中执行。）
*   **Stop order**： Used for **protection** （limit loss or lock in gains）。 （止损单：用于**保护**（限制损失或锁定收益）。）
*   **Buy stop order**： Protects a short position。 Triggered if the market price touches a particular price or **higher**。 （**买入止损单**：保护空头头寸。如果市场价格达到特定价格或**更高**时触发。）
*   **Sell stop order**： Protects a long position。 Triggered if the market price touches a particular price or **lower**。 （**卖出止损单**：保护多头头寸。如果市场价格达到特定价格或**更低**时触发。）
*   **Limit order**： Used when a customer is specific about the price。 （限价单：当客户对价格有具体要求时使用。）
*   **Buy limit**： Buy at the limit price or **lower**。 （**买入限价**：按限价或**更低**价格买入。）
*   **Sell limit**： Sell at the limit price or **higher**。 （**卖出限价**：按限价或**更高**价格卖出。）

🧠 **REMEMBER**
Because stop and limit orders are price-specific, they **may or may not be executed**.
🧠 **请记住**
由于止损单和限价单对价格有特定要求，它们**可能成交，也可能不成交**。

---

## 5. Factoring in order features
## 5. 考虑订单特征

*   **Day**： Canceled if not filled by the end of the trading day。 （当日有效单：如果交易日结束前未成交则取消。）
*   **Good-'til-canceled （GTC）**： Open until executed or canceled。 （撤销前有效单 （GTC）：一直开启，直到执行或被撤销。）
*   **Not held （NH）**： Gives the broker discretion about **timing**。 NH orders deal only with timing， not the security or quantity。 （不限时订单 （NH）：赋予经纪人在**时机选择**上的自主权。NH 订单仅涉及择时，不涉及证券品种或数量。）
*   **Fill or kill （FOK）**： Execute **entire order immediately** or cancel。 （全额成交或取消 （FOK）：**立即全额执行**订单，否则取消。）
*   **Immediate or cancel （IOC）**： Execute as much as possible immediately； cancel the rest。 （立即成交或取消 （IOC）：立即执行尽可能多的部分，取消剩余部分。）
*   **All-or-none （AON）**： Execute in entirety or not at all （doesn't have to be immediate）。 （全额成交 （AON）：要么全额执行，要么不执行（不一定非要立即执行）。）

---

## 6. Recognizing Different Types of Investors
## 6. 识别不同类型的投资者

*   **Retail investors**： Nonprofessionals trading for their own accounts。 （散户投资者：为自己的账户进行交易的非专业人士。）
*   **Accredited investors**： Investors with more money or knowledge。 Includes financial institutions， insiders， and individuals with an **annual income of $200,000** （$300,000 joint） or a **net worth of $1 million** （excluding primary residence）。 （合格投资者：拥有更多资金或知识的投资者。包括金融机构、内幕人士，以及**年收入达 20 万美元**（夫妻共有 30 万美元）或**净资产达 100 万美元**（不包括主要住所）的个人。）
*   **Institutional investors**： Entities that invest a lot of money （e。g。， banks， mutual funds， pension funds）。 （机构投资者：投入大量资金的实体（如银行、共同基金、养老基金）。）

---

## 7. Testing Your Knowledge
## 7. 知识测试

Practice questions (Original English Only)

1. Which two of the following are TRUE?
   I. Dealers charge a markup or markdown for trades. II. Dealers charge a commission for trades. III. Brokers charge a markup or markdown for trades. IV. Brokers charge a commission for trades.
   (A) I and III (B) I and IV (C) II and III (D) II and IV

2. Which of the following best describes a third market trade?
   (A) Exchange-listed securities trading OTC
   (B) Exchange-listed securities trading on the exchange floor
   (C) Unlisted securities trading OTC
   (D) Institutional trading without using the services of a broker-dealer

3. Which of the following orders would protect a short position?
   (A) Buy limit (B) Sell limit (C) Buy stop (D) Sell stop

4. If an at-the-open order is not executed at the opening price, what happens to the order?
   (A) It is canceled. (B) It becomes a market order. (C) It becomes a day order. (D) It becomes a limit order.

5. An investor with no other positions would like to purchase ABC common stock, which is currently trading at $30.80. If this investor is interested in purchasing the stock for $28 or less, you should suggest the investor enters a
   (A) buy stop limit order (B) buy limit order (C) buy stop order (D) market order

6. Which of the following would be considered accredited investors?
   I. Banks II. An individual investor with a net worth of $2 million, excluding her primary residence III. A corporation with a net worth of $10 million IV. Insurance companies
   (A) II and IV (B) I and IV (C) I, III, and IV (D) I, II, III, and IV

7. Which TWO of the following are TRUE of short sellers?
   I. They are taking a bullish position. II. They are taking a bearish position. III. They have a maximum gain potential that is unlimited. IV. They have a maximum loss potential that is unlimited.
   (A) I and III (B) I and IV (C) II and III (D) II and IV

8. A not-held order gives a broker discretion as to
   (A) which security is traded (B) the time at which a security is traded (C) whether to purchase, sell, or sell short a security (D) all of the above

### Answers and explanations

1.  **B.** Dealers act as principals and charge markups/markdowns. Brokers act as agents and charge commissions.
2.  **A.** The third market involves listed securities trading in the OTC market.
3.  **C.** A buy stop order protects short positions by triggering a purchase if the price rises.
4.  **A.** At-the-open orders must be executed at the start of trading or be canceled.
5.  **B.** A buy limit order allows an investor to buy at a specific price or lower.
6.  **D.** All choices meet the criteria for accredited investors (institutions and high-net-worth individuals).
7.  **D.** Short sellers are bearish and face unlimited loss potential because there is no cap on how high a stock price can rise.
8.  **B.** Not-held (NH) orders only give the broker discretion over the **timing** and **price** of the execution.


### Additional Practice Questions

9. Which of the following order features allows for partial execution?
$ FOK
% AON
& IOC
' All of the above
10. Which TWO of the following are FALSE regarding unsolicited orders?
I. They cannot be accepted without prior approval from a principal.
II. They can be accepted without prior approval from a principal.
III. They must be limited in size.
IV. They are not limited in size.
$ I and III
% I and IV
& II and III
' II and IV
11. A market maker quotes a stock at 18.10 - 18.30, 20 x 25. This means the market maker is willing to:
$ Sell 2,500 shares at $18.10 and buy 2,000 shares at $18.30
% Buy 2,000 shares at $18.10 and sell 2,500 shares at $18.30
& Sell 250 shares at $18.10 and buy 200 shares at $18.30
' Buy 200 shares at $18.10 and sell 250 shares at $18.30
12. Mary and Eohn have been married for several years. They have a combined income that has
exceeded $300,000 per year for the last four years and is expected to at least be that much for
the current year. They would be considered a(n)
$ qualified institutional buyer (QIB)
% accredited investor
& institutional investor
' bank qualified investor
13. WY Broker-Dealer charges a commission on a securities transaction. WY Broker-Dealer has
acted as a(n)
$ agent
% principal
& market maker
' dealer
CHAPTER   6ecurities Markets Taking 2rders and Executing Trades  241
14.
“Spread” in the over-the-counter (OTC) market refers to the difference between the
$ highest bid and lowest ask price
% lowest offer price and highest ask price
& the opening and closing prices of a particular security
' the “when issued” ask price
15. Marvin Plimpton is an associated person but is not a licensed registered representative. Which
of the following activities is Marvin permitted to engage in?
$ Accepting unsolicited orders from a customer who resides in the same state
% Discussing the plusses and minuses of a particular investment to an existing customer of
the firm
& Forwarding account opening forms to a new customer
' Discussing investment obÛectives with a potential customer prior to handing the customer
over to a licensed registered representative
242 PART   Playing Nicely: Serving Your Client’s Needs and Following the Rules

### Additional Answers

9. C. If you remember what the initials stand for, it makes the question a lot easier. FOK
stands for fill or kill, which means that the entire order must be either filled immediately or
killed (canceled). AON stands for all-or-none, which means that the entire order must be
filled entirely (but not immediately) or none of the order gets executed. The one that allows
for partial execution is an IOC (immediate or cancel) order, which means that the broker
has to execute as much of the order as possible immediately and cancel the rest.
10. A. Remember, you’re looking for false answers to this question. Unsolicited orders are
ones in which the investor tells the registered rep which securities they want to purchase,
sell, or sell short. Although orders must be approved by a principal, they don’t have to
be approved prior to the order being placed. In addition, there are no limits to the size
of the order regarding unsolicited orders; they are only limited based on the investor’s
ability to pay.
CHAPTER   6ecurities Markets Taking 2rders and Executing Trades  243
11.
B. The first price (18.10) is the bid price (the price at which the market maker is willing to
purchase the security). The second price (18.30) is the ask price that the market maker is
willing to accept when selling the security. The “20x25” represents the number of round
lots the market maker is willing to buy or sell. Unless told differently, a round lot is 100
shares. Therefore, the market maker is willing to buy up to 2,000 shares at $18.10 and sell
up to 2,500 shares at $18.30.
12. B. As a married couple, accredited investors are ones that have a Ûoint income of at least
$300,000 for the previous two years and is expected to be at least $300,000 for the current
year.
13. A. Brokers act as middlemen in a securities transaction. They’re putting a buyer and seller
together to make a trade. As such, they charge a commission. A good way to remember this
is to think of a real estate agent or broker. Real estate agents or brokers charge a commis-
sion for selling someone else’s house to a buyer.
14. A. The term “spread” refers the difference between the highest bid price (the most a
market maker is willing to pay to purchase the security) and the lowest ask (offer) price
(the least a market maker will take when selling the security). Typically, the narrower the
spread, the more actively traded the security.
15. C. Since Marvin is not licensed, he cannot discuss anything relating to investments with an
existing customer or potential customer. If he cannot do that, he certainly cannot accept
orders (whether solicited or not) from a customer. However, he can do things such as
sending account opening forms to a new customer.
CHAPTER   Making 6ure the Ζ56 *ets Ζts 6hare  245
Making Sure the IRS
*etsbΖts 6hare
Y
es, it’s true what they say: The only sure things in life are death and taxes. Although taxes
are an annoying necessity, investors do get tax breaks if they invest in securities for a long
period of time — which means you, as a rep, need a good understanding of the tax dis-
counts investors could potentially receive. Additionally, the SIE exam tests your ability to recog-
nize the different types of retirement plans, the specifics about each one, and the tax advantages.
In  this  chapter,  I  cover  tax  categories  and  rules,  from  distinguishing  among  types  of  taxes  to
types of income. And although enjoying retirement isn’t quite as certain as pushing up daisies, I
explain Uncle Sam’s claim on the cash investors put into 401(k)s, individual retirement accounts
(IRAs), and other retirement plans. As always, you can count on some example questions and an
exam at the end of the chapter to wrap it up.
Everything in Its Place: Checking Out
Tax and Income Categories
The many lines you see on tax forms clue you in to the fact that the Internal Revenue Service (IRS)
likes to break things into categories. The following sections explain progressive and regressive
taxes, as well as types of personal income.
Chapter 15
IN THIS CHAPTER
»Outlining the breakdown of taxes
and income
»Seeing how the IRS taxes securities
»&omparing the di΍erent types oI
retirement plans
»Taking a practice quiz
246 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
Touring the tax categories
The supreme tax collector (the IRS) has broken taxes into a couple of categories, according to the
percentage individuals pay. Your mission is to understand the different tax categories and how
they affect investors:
»
Progressive taxes: These ta[es a΍ect highincome individuals more than they a΍ect low
income individuals the more ta[able income individuals have, the higher their income ta[
bracket. Progressive ta[es include ta[es on personal income (see the ne[t section), gift ta[es,
and estate ta[es. The SIE contains more Tuestions on progressive ta[es than on regres
sive ta[es.
»
Regressive taxes: These ta[es a΍ect individuals earning a lower income more than they a΍ect
people earning a higher income everyone pays the same rate, so individuals who earn a lower
income are a΍ected more because that rate represents a higher percentage of their income.
E[amples of regressive ta[es are payroll ta[es, sales ta[es, property ta[es, e[cise ta[es,
gasoline ta[es, and so on.
Looking at types of income
The  three  main  categories  of  income  are  earned,  passive,  and  portfolio.  (If  you’re  especially
interested in the details of how investments are taxed, you can find more information at
www.
irs.gov
.) You need to distinguish among the different categories because the IRS treats them
differently:
»
Earned (active) income: People generate this type of income from activities that theyȇre
actively involved in. Earned income includes money received from salary, bonuses, tips,
commissions, and so on. Earned income is ta[ed at the individualȇs ta[ bracket and based on
their ȴling status.
»
Passive income: This type of income comes from enterprises in which an individual isnȇt
actively involved. Passive income includes income from limited partnerships (see Chapter 0)
and rental property. :hen you see the words passive income on the SIE e[am, immediately
start thinking that the income comes from a direct participation program ('PP). Individuals can
write o΍ passive losses against any passive income to determine the net ta[able income.
»
Portfolio income: This type of income includes interest, dividends, and capital gains derived
from the sale of securities. The following section tells you more about ta[es on portfolio
income. Portfolio income may be ta[ed at the investorȇs ta[ bracket or at a lower rate,
depending on the holding period.
Noting Taxes on Investments
You need to understand how dividends, interest, capital gains, and capital losses affect investors.
To make your life more interesting, the IRS has given tax advantages to people who hold onto
investments for a long period of time, so familiarize yourself with the types of taxes that apply to
investments and how investors are taxed.
CHAPTER   Making 6ure the Ζ56 *ets Ζts 6hare  247
Interest income
Interest income that bondholders receive may or may not be taxable, depending on the type of
security or securities held:
»
Corporate bond interest: Interest received from corporate bonds is ta[able at all levels
(federal, state, and local, where local ta[es e[ist).
»
Municipal bond interest: Interest received from most municipal bonds (e[cept ta[able
municipals) is federally ta[free however, investors may be ta[ed on the state and local levels,
depending on where the investor lives and the municipality of the issuer of the bonds. (See
Chapter .)
»
U.S. government securities interest: Interest received from 8.S. government securities, such
as Tbills, Tnotes, TSTRIPS, TIPS, and Tbonds, is ta[able on the federal level but e[empt from
state and local ta[es.
Even though T-bills, T-STRIPS, and any other zero-coupon bonds don’t generate interest pay-
ments (because the securities are issued at a discount and mature at par, which is the face value
of the security), the difference between the purchase price and the amount received at maturity
is considered interest and is subject to taxation.
Dividends
Dividends may be in the form of cash, stock, or product. The following sections discuss dividends
in cash, in stock, and from mutual funds.
Cash dividends
Qualified  cash  dividends  received  from  stocks  are  taxed  at  a  maximum  rate  of  0  percent,
15 percent, or 20 percent, depending on the investor’s adÛusted gross income (AGI). Qualified
dividends are ones in which the customer has held onto the stock for at least 61 days (91 days for
preferred stock). The 61-day holding period starts 60 days prior to the ex-dividend date (the first
day the stock trades without dividends). If the investor has held the stock for less than the 61-day
holding  period,  the  dividends  are  considered çïçþĒÞifie±Ⱦ  and  investors  are  taxed  at  the  rate
determined by their regular tax bracket.
Note: There is currently an additional net investment tax of 3.8 percent for individual investors
with a modified adÛusted gross income above $200,000 ($250,000 for married couples).
Stock dividends
Stock dividends don’t change the overall value of investment, so additional shares received are
not taxed. (For details, see Chapter 6.) However, stock dividends do lower the cost basis per share
for tax purposes. The cost basis is used to calculate capital gains and losses.
Dividends from mutual funds
Dividends  and  interest  generated  from  securities  that  are  held  in  a  mutual  fund  portfolio  are
passed  through  to  investors  and  are  taxed  as  either þĒÞifie±  (see  the  earlier  section  “Cash
dividends”) or çïçþĒÞifie±. The type(s) of securities in the portfolio and the length of time the
248 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
fund held the securities dictate how the investor is taxed. Here’s how mutual fund dividends are
taxed:
Federally Tax-Free0, 15, or 20 PercentOrdinary Income
0unicipal bond fundsStock fundsCorporate bond funds
/ongterm capital gainsShortterm capital gains
One of the great things about owning mutual funds is that they’re nice enough to let you know
what taxes you’re going to be subject to. At the beginning of each year (usually in January), you
receive a statement from the mutual fund that lets you know how much you received the previous
year in dividends, in short-term capital gains, and in long-term capital gains. The mutual fund
also sends a copy of the statement to the IRS.
The mutual fund determines the long-term or short-term gains by its holding period, not the
investors’. Also, remember that you’re subject to capital gains tax and taxes on dividends each
year even if the money is reinvested in the fund.
At the sale: Capital gains and losses
Capital gains are profits (realized gains) made when selling a security, and capital losses are losses
incurred when selling a security. To determine whether an investor has a capital gain or capital
loss, you have to start with the investor’s cost basis. The cost basis is used for tax purposes and
includes the purchase price plus any commission (although on the SIE exam, the test designers
usually don’t throw commission into the equation). The cost basis remains the same unless it’s
adjusted for things like stock splits, stock dividends, accretion, amortization, and so on.
Accretion and amortization come into play when an investor purchases a bond at a price other
than par. The bond cost basis will be adjusted toward par over the amount of time until maturity.
You won’t be asked to calculate it on the SIE exam.
Incurring taxes with capital gains
An investor realizes capital gains when they sell a security at a price higher than their cost basis.
Capital gains on any security (even municipal and U.S. government bonds) are fully taxed on the
federal, state, and local levels.
A capital gain isn’t realized until a security is sold.
Note: If the value of an investment increases, it’s considered appreciation or an unrealized gain,
and if the investor doesn’t sell, the investor doesn’t incur capital gains taxes. Mutual fund share-
holders would be subÛect to taxation if the issuer sold securities held by the fund at a profit, even
if the shareholder didn’t sell any shares.
Capital  gains  are  broken  down  into  two  categories,  depending  on  the  holding  period  of  the
securities:
»
Short-term capital gains: These gains are reali]ed when a security is held for one year or less.
Shortterm capital gains are ta[ed according to the investor’s tax bracket.
CHAPTER   Making 6ure the Ζ56 *ets Ζts 6hare  249
»
Long-term capital gains: These gains are reali]ed when a security is held for more than one
year. To encourage investors to buy and hold securities, longterm capital gains are currently
ta[ed at a rate in line with cash dividends (0, , or 20 percent depending on the investorȇs
adMusted gross income). )or more information on capital gains and losses, visit the IRS website
at
www.irs.gov/taxtopics/tc409.
Note: If an investor purchased 100 shares of a particular security for $4,000 and later sold those
shares for $6,000, the original $4,000 purchase price would be considered a return of capital. Only
the $2,000 capital gain ($6,000 selling price minus the $4,000 purchase price) would be taxable.
So, the taxes would be based upon the profit made (how much was made above the investor’s
cost basis).
2΍setting gains with capital losses
Certainly, no matter how much research has been done, not every investment is going to be prof-
itable. An investor realizes a capital loss when selling a security at a value lower than the cost
basis. Investors can use capital losses to offset capital gains and reduce the tax burden. Like capi-
tal gains, capital losses are broken into short-term and long-term:
»
Short-term capital losses: An investor incurs these losses when they have held the security
for one year or less. Investors can use shortterm capital losses to o΍set shortterm cap
ital gains.
»
Long-term capital losses: An investor incurs these losses when they have held the security
for more than one year. /ongterm capital losses can o΍set longterm capital gains.
When an investor has a net capital loss, they can write off up to $3,000 per year on their federal
taxes against their earned income and carry the balance forward to the following year. Married
couples filing Ûointly can write off $3,00 per year, and married couples filing separately can write
off $1,500 per year each. For test purposes, assume $3,000 per year.
The following question involves capital-loss write-offs.
In a particular year, Eones realizes $30,000 in long-term capital gains and $50,000 in
long-term capital losses. How much of the capital losses would be carried forward to the
following year?
(A) $3,000
(B) $17,000
(C) $20,000
(D) $30,000
The correct answer is (B). Eones has a net capital loss of $20,000 (a $50,000 loss minus the
$30,000 gain). Eones writes off $3,000 of that capital loss against the earned income and carries
the additional loss of $17,000 forward to write off against any capital gains they may have in
future years. In the event that Jones doesn’t have any capital gains the following year, they can
still write off $3,000 of the $17,000 against any earned income and carry the remaining $14,000
forward, which can be used to offset any capital gains the following year. The loss can be carried
forward to subsequent years until used up or the investor dies.
250 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
The wash sale rule: Adjusting the cost basis
when you can’t claim a loss
To keep investors from claiming a loss on securities (which an investor could use to offset gains
on another investment; see the preceding section) while repurchasing substantially (or exactly)
the same security, the IRS has come up with the wash sale rule. According to this rule, if an inves-
tor sells a security at a capital loss, the investor can’t repurchase the same security or anything
convertible into the same security for 30 days prior to or after the sale and be able to claim the
loss. An investor doesn’t end up in handcuffs for violating the wash sale rule; they simply can’t
claim the loss on their taxes.
However, the loss doesn’t go away if investors buy the security within that window of time;
investors get to adjust the cost basis of the security. If an investor were to sell 100 shares of ABC
at a $2-per-share loss and purchase 100 shares of ABC within 30 days for $50 per share, the
investor’s new cost basis (excluding commissions) would be $52 per share (the $50 purchase
price plus the $2 loss on the shares sold), thus lowering the amount of capital gains they would
face on the new purchase.
The following question tests your understanding of the wash sale rule.
If Melissa sells DEF common stock at a loss on June 2, for 30 days they can’t buy which of the
following securities without being subject to the wash sale rule?
I. 'E) common stock
II. 'E) warrants
III. 'E) call options
IV. 'E) preferred stock
(A)
I only
(B) I and IV only
(C) I, II, and III only
(D) I, II, III, and IV
The answer you want is (C). You need to remember that Melissa sold DEF at a loss; therefore, they
can’t buy back the same security (as in statement I) or anything convertible into the same secu-
rity  (as  in  statements  II  and  III)  within  30  days  to  avoid  the  wash  sale  rule.  Warrants  give  an
investor the right to buy stock at a fixed price (see Chapter 6), and call options give investors the
right to buy securities at a fixed price (Chapter 11). However, statement IV is okay because DEF
preferred stock is a different security and is not convertible into DEF common stock (unless it’s
convertible preferred, which it isn’t; if it were convertible, the question would have told you so).
For Melissa to avoid the wash sale rule, they can’t buy DEF common stock, DEF convertible pre-
ferred stock, DEF convertible bonds, DEF call options, DEF warrants, or DEF rights for 30 days.
However, they can buy DEF preferred stock, DEF bonds, or DEF put options (the right to sell DEF).
Putting it in simple terms, the cost basis is the price an individual paid for an investment after
taxes. This cost includes brokerage fees, trading costs, and loads (sales charges for mutual funds).
Now, things can get a little more complex in the event of stock splits, mergers, and dividend pay-
ments. The main thing that you need to know for the SIE exam is that the cost basis is used for
calculations to determine an investor’s tax liability when selling securities. More recently, bro-
kerage firms, mutual funds, and so on are required to provide investors information on their tax
liability,  such  as  the  amount  of  short-term  capital  gains,  long-term  capital  gains,  dividends,
interest, and so on.
CHAPTER   Making 6ure the Ζ56 *ets Ζts 6hare  251
Estate taxes
Estate tax  is  a  tax  on  property  that  is  passed  along  to  someone’s  estate  when  the  person  dies.
Inheriting securities is a little more straightforward than receiving gifts of securities. When an
individual receives securities as a result of an inheritance, they always assume the fair market
cost  basis  of  the  inherited  securities  on  the  date  of  the  owner’s  death.  Additionally,  securities
received  by  inheritance  are  always  assigned  a  long-term  holding  characterization  for  tax
purposes when sold. Estate taxes are covered a little more in depth in the Series 7 book.
Exploring Retirement Plan Tax Advantages
I place retirement plans with taxes because retirement plans give investors tax advantages. When
you’re reviewing this section, zone in on the differences and similarities among the different
types of plans. The contribution limits are important but not as important as understanding the
plan specifics and who’s qualified to open which type of plan.
Qualified Yersus nonqualified plans
The  IRS  may  dub  employee  retirement  plans  as  qualified  or  nonqualified.  The  distinction
concerns  whether  they  meet  IRS  and  Employee  Retirement  Income  Security  Act  (ERISA)
standards for favorable tax treatment.
Taxqualified plans
A tģɔþĒÞifie± ûÞç  meets  IRS  standards  to  receive  a  favorable  tax  treatment.  When  you’re
investing in a tax-qualified plan, the contributions into the plan are made from pretax dollars and
are excluded from your taxable income. Not only are contributions into the plan excluded from
income,  but  the  account  also  grows  on  a  tax-deferred  basis,  so  you  aren’t  taxed  until  you
withdraw money from the account at retirement. IRAs are examples of tax-qualified retirement
plans. The two types of corporate tax-qualified retirement plans are defined contribution and
defined benefit plans. These include 401(k)s, profit-sharing plans, and money-purchase plans.
Most corporate pension plans are tax-qualified plans.
Because investors don’t pay tax on the money initially deposited or on the earnings, the entire
withdrawal from a tax-qualified plan is taxed at a rate determined by the investor’s tax bracket,
which is normally lower during retirement. Additionally, distributions taken before age 59½ are
subject  to  a  10  percent  tax  penalty  (10  percent  additional  tax  on  early  distributions)  except  in
cases  of  death,  disability,  first-time  home  buying,  educational  expenses  for  certain  family
members, medical premiums for unemployed individuals, and so on.
1onqualified plans
Obviously, a nonqualified plan is the opposite of a qualified plan. SïçþĒÞifie± ûÞçsȾ  such  as
deferred compensation plans, payroll deduction plans, and 457 plans, do not meet IRS and ERISA
standards  for  favorable  tax  treatment.  If  you’re  investing  in  a  nonqualified  retirement  plan,
deposits are not tax-deductible (they’re made from after-tax dollars); however, because you’re
dealing with a retirement plan, earnings in the plan do build up on a tax-deferred basis. People
may choose to invest in nonqualified plans because either their employer doesn’t have a qualified
plan  set  up  or  the  investment  guidelines  are  not  as  strict  (investors  may  be  able  to  contribute
more and invest in a wider choice of securities).
252 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
Because investors have already paid tax on the money initially deposited but not on the earnings,
withdrawals  from  nonqualified  plans  are  only  partially  taxed  at  the  rate  determined  by  the
investor’s  tax  bracket.  The  investor  is  taxed  only  on  the  amount  that  exceeds  the  amount  of
the contributions made.
IRA types and contribution limits
You’ll likely be tested on a few different types of retirement plans and possibly the contribution
limits. When you’re looking at this section, understand the specifics of the types of plans and
view the contribution limits as secondary. The contribution limits change pretty much yearly,
and the SIE questions may not change that often. If you have a rough idea of the contribution
limits, you should be okay. For updates and additional information, you can go to
www.irs.gov/
retirement-plans/plan-participant-employee/retirement-topics-ira-
contribution-limits
.
Traditional IRAs
IRAs (Individual Retirement Accounts or Individual Retirement Arrangements) are tax-qualified
retirement  accounts,  so  deposits  in  the  account  are  made  from  pretax  dollars.  (They’re  tax-
deductible.)  IRAs  are  completely  funded  by  contributions  that  the holder of the account  makes.
Regardless of whether individuals are covered by a pension plan, they can still deposit money in
an IRA. Here’s a list of some of the key points of IRAs:
»
IRAs may be set up as single life (when the owner is the beneȴciary of the account), joint and
last survivor (when the sole beneȴciary of the account is their spouse and the spouse is more
than ten years younger than the owner), or uniform lifetime (when the spouse is not the sole
beneȴciary or the spouse is not more than ten years younger than the owner).
»
Permissible investments for IRAs include stocks, bonds, mutual funds, 8.S. gold and silver
coins, and real estate.
»
The ma[imum contribution per person as of 202 (which increased from 6,00 from 2023) is
,000 per year, with an additional catchup contribution of ,000 per person allowed for
investors age 0 or older. E[cess contributions are ta[ed at a rate of 6 percent per year until
the e[cess is withdrawn.
»
As of 202, a husband and wife under age 0 can have separate accounts with a ma[imum
contribution of ,000 per year each, whether both are working or one is working.
»
Contributions to the IRA are fully deductible for individuals not covered by employer
pension plans.
If investors are covered by a workplace retirement plan, deposits into an IRA may or may
not be ta[deductible. Although I think that the chances of your being tested on the values are
slim, as of 202, if an individual is covered by a workplace retirement plan and earns up to
,000 per year (23,000 Mointly), deposits made into an IRA are fully deductible. The deduc
tions are gradually phased out and disappear when an individual earns more than ,000 per
year (3,000 for married couples ȴling Mointly).
»
:hen an investor starts to withdraw funds from an IRA, the investor is ta[ed on the entire
withdrawal (the amount deposited, which was not ta[ed, and the appreciation in value). The
withdrawal is ta[ed as ordinary income.
»
:ithdrawals canȇt begin before age , or investors have to pay an early withdrawal penalty
of 0 percent added to the investorȇs rate according to their ta[ bracket. An investor isnȇt
CHAPTER   Making 6ure the Ζ56 *ets Ζts 6hare  253
subMect to the 0 percent ta[ penalty in cases of death, disability, ȴrsttime homebuyers, and a
few other e[ceptions. (2bviously, dead retirees wonȇt be making withdrawals, but their
beneȴciaries will be in this case, the beneȴciaries arenȇt hit with the 0 percent penalty.)
»
:ithdrawals must begin by April  of the year after the investor reaches age 3 (the required
beginning date, or R%'). Investors who donȇt take their required minimum distribution (R0') by
that time are subMect to a 0 percent ta[ penalty on the amount they should have withdrawn.
The IRS provides minimum distribution worksheets to help you determine the amount that
needs to be withdrawn in order to avoid the penalty you can ȴnd them at
www.irs.gov/
retirement-plans/plan-participant-employee/required-minimum-distribution-
worksheets
.
»
'eposits in IRAs are allowed up to April  (Ta[ 'ay) to Tualify as a deduction for the previous
yearȇs ta[es.
Roth IRAs
Anyone whose income is below the IRS modified adÛusted gross income limit can open a Roth
IRA. The key difference between a traditional IRA and a Roth IRA is that withdrawals from a
Roth IRA are not taxed. However, deposits made in the Roth IRA are not tax-deductible (made
from after-tax dollars). Provided that the investor has held onto the Roth IRA for more than five
years and has reached age 59½, they can withdraw money from the Roth IRA without incurring
any taxable income on the amount deposited or on the appreciation in the account. So, in this
case, all qualified distributions are excluded from federal income tax.
As of 2024, the maximum that an individual may contribute to a traditional IRA and Roth IRA is
$7,000 per year combined. There is also a catch-up contribution of $1,000 allowed for individuals
age 50 and older, which means they can contribute up to $8,000 per year.
As of 2024, investors who have an adÛusted gross income of more than $161,000 per year ($240,000
married, filing Ûointly) can’t contribute to a Roth IRA.
6implified employee pensions 6E3Ζ5$s
An SEP-IRA is a retirement vehicle designed for small-business owners, self-employed individu-
als, and their employees. SEP-IRAs allow participants to invest money for retirement on a tax-
deferred  basis.  Employers  can  make  tax-deductible  contributions  directly  to  their  employees’
SEP-IRAs.  As  of  2024,  the  maximum  employer  contribution  to  each  employee’s  SEP-IRA  is
25 percent of the employee’s compensation (salary, bonuses, and overtime) or $69,000 (subÛect
to cost-of-living increases in the following years), whichever is less. Employees who are part of
the plan may still make annual contributions to a traditional or Roth IRA.
401(k) and 403(b)
There are certainly a number of qualified retirement plans besides IRAs. 401(k)s and 403(b)s are
two that you should know a little about before taking the SIE exam.
401(k) plans
As stated previously, a 401(k) is a corporate retirement plan. With this type of plan, employees
can  contribute  a  percentage  of  their  salary  up  to  a  certain  amount  each  year  (as  such,  it’s  a
defined contribution plan). Because it’s a qualified plan, the amount contributed by the employee
to  the  401(k)  is  excluded  from  the  employee’s  gross  income.  In  addition,  in  most  cases,  the
254 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
employer matches the employee’s contribution up to a certain amount (for example, 25 percent,
50 percent, and so on). The account grows on a tax-deferred basis, so everything withdrawn from
the account at retirement is taxable.
Roth 401(k) plans
A Roth 401(k) has similarities between traditional 401(k) plans and Roth IRAs. As with a tradi-
tional 401(k), the contribution limits, which adjust yearly, are the same as well as the fact that
they are both employer-sponsored plans. However, like a Roth IRA, contributions are made after
taxes. So, withdrawals of contributions and earnings are not taxed as long as the account has been
held for at least five years and the holder is at least 59ȳ years old (except in cases of death or
disability). Unlike Roth IRAs, required minimum distribution (RMD) rules apply.
Note: Roth 401(k)s are like Roth IRAs because qualified distributions are excluded from federal
income tax.
403(b) plans
These are salary reduction plans for public school (elementary school, secondary school, college,
and so on) employees, tax-exempt organizations, and religious organizations. These plans are
also known as tax-sheltered annuities. As with 401(k)s, employees can elect to have a portion of
their pay put into the retirement plan that’s tax deferred. Like 401(k)s, the employer may match
a percentage of the contributions. To be eligible, employees must be at least 21 years old and have
been working for the employer for at least a year.
Because the IRS wants to be able to collect taxes, the holders of IRAs (except for Roth IRAs) and
other qualified-plan participants must start withdrawing money at a certain point. Plan partici-
pants must take a required minimum distribution (RMD) by April 1 of the year after they turn age
73, whether they need the money at that point or not. In addition, they must continue to take
additional minimum distributions each subsequent year until all the money is out of the account.
Testing Your Knowledge
Following is a small sample of questions you may see related to taxes and retirement plans on the
SIE exam. Read each question carefully. Good luck!
Practice questions
1. Which of the following are regressive taxes?
I. Sales
II. Income
III. Gasoline
IV. Alcohol
(A) III and IV
(B) I, II, and III
(C) I, III, and IV
(D) I, II, III, and IV
CHAPTER   Making 6ure the Ζ56 *ets Ζts 6hare  255
2.
All of the following are types of tax-qualified retirement plans ECEPT
(A) 401(k)
(B) profit-sharing
(C) IRA
(D) deferred compensation
3. Which of the following are TRUE regarding Roth IRAs and Roth 401(k)s?
(A) Withdrawals from both are tax-free provided that investors have held the accounts
for at least five years and have reached the age of 59ȳ.
(B) There are no contribution limits.
(C) Contributions made to both are made pretax.
(D) All of the above.
4. An investor buys 1,000 shares of a stock at $30. If the stock increases in value to $50, how
would the result be categorized?
(A) Profit
(B) Appreciation
(C) Capital gain
(D) Investment income
5. An individual investor who lives at home with their parents is covered by an employer pension
plan. However, they would like more coverage at retirement and decides to put the maximum
allowable contribution in an IRA. If their salary is $52,000 per year, which of the following is
TRUE?
(A) Contributions to the IRA are fully deductible.
(B) Contributions to the IRA are partially deductible.
(C) Contributions to the IRA are not deductible.
(D) Cannot be determined.
6. Which of the following is taxable for an investor for the year in which it occurs?
I. Stock dividends
II. Cash dividends
III. Interest received from corporate bonds
IV. Interest received from U.S. government bonds
(A) I, II, and III
(B) II and III
(C) II, III, and IV
(D) I, II, III, and IV
256 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
7. A customer purchased 100 shares of ABC stock at $40 per share on March 24. On March 24 of
the following year, the customer sold the stock at $46 per share. Which TWO of the following
are TRUE regarding these transactions?
I. They would be taxed as a short-term capital gain.
II. They would be taxed as a long-term capital gain.
III. The gain would be taxed at the customer’s tax bracket.
IV.  The gain would be taxed at 0 percent, 15 percent, or 20 percent, depending on the
customer’s adjusted gross income.
(A) I and III
(B) I and IV
(C) II and III
(D) II and IV
8. According to the wash sale rule, if a customer sold a security at a loss, which of the following
is TRUE?
(A) The customer cannot purchase call options on the same security for 30 days before or
after the sale and be able to claim the loss.
(B) The customer cannot purchase bonds by the same issuer for 30 days before and after the
sale and be able to claim the loss.
(C) The customer cannot sell short the same security within 30 days before or after the sale
and be able to claim the loss.
(D) The customer cannot purchase mutual funds holding the same security for 30 days before
and after the sale and be able to claim the loss.
9. Which of the following types of retirement plans is a salary reduction plan set up for public
school employees?
(A) SEP-IRAs
(B) 401(k)s
(C) 403(b)s
(D) Keogh plans
CHAPTER   Making 6ure the Ζ56 *ets Ζts 6hare  257
Answers and explanations
1. C. Regressive taxes are ones in which all individuals are charged the same percentage
regardless of their income. Sales tax, gasoline tax, and alcohol tax are all regressive taxes.
Income tax is a progressive tax because the higher your income, the higher the tax bracket.
2. D. Tax-qualified plans are ones that meet IRS standards for favorable tax treatment. If the
plan is tax-qualified, contributions are made from pretax dollars. However, when the
money is withdrawn, the entire amount, including the initial contributions plus any gains,
is taxable. Tax-qualified plans include IRAs, 401(k)s, profit-sharing, money-purchase, and
so on. Nonqualified plans are funded from after-tax contributions and include deferred
compensation, payroll deduction, 457 plans, and so on.
3. A. Contributions to both Roth IRAs and Roth 401(k)s are made from after-tax dollars. So,
withdrawals are tax-free provided that investors have held the accounts for at least five
years and are at least 59½ years old.
4. B. In this case, because the investor didn’t sell the security at a profit, in which case it
would’ve been a capital gain, it is categorized as appreciation.
5. A. An investor can always contribute money to an IRA even if covered by an employer
pension plan. However, whether it’s deductible depends on the investor’s earnings. As
of 2024 (the amount increases yearly), an investor who makes up to $77,000 can
contribute to an IRA and be able to deduct the full amount from their taxes.
6. C. Cash dividends, interest from corporate bonds, and interest from U.S. government bonds
are all taxable for the year in which they occurred. However, stock dividends are not taxable
because the investor didn’t receive a payment, just more shares of stock, which lowered the
cost basis.
7. A. This is a short-term capital gain because when a security is sold up to and including one
year from the purchase date, it would be a short-term capital gain or loss. Because it is
short-term, the gain would be taxed at the investor’s tax bracket.
8. A. According to the wash sale rule, an investor who is selling a security at a loss cannot
purchase the same security or anything convertible into the same security for 30 days
prior or 30 days after the sale and be able to claim the loss. However, the loss isn’t gone
completely; it just means that the cost basis for the new securities purchased will be
adjusted for the loss. So, if the investor sold ABC common stock at a loss, they wouldn’t
be able to purchase ABC call options on the stock because call options give the investor
the right to purchase the underlying security.
9. C. 403(b) plans are set up for public school employees (elementary, secondary, college, and
so on). They are considered salary reduction plans because the amount contributed by the
employee reduces their salary so that they aren’t taxed on the money contributed until it’s
taken out at retirement.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  259
Rules and Regulations:
1ob)ooling $round
F
irst off, I’d like to apologize for having to include this chapter. Unfortunately, rules are a part
of life and part of the SIE. When you’re reading this, please remember that I didn’t make
the rules — but I do my best to make them as easy to digest as possible. Rules have become
increasingly important on FINRA securities exams like the SIE, especially since the Patriot Act
came into the picture.
In this chapter, I cover topics related to rules and regulations. First, I help you understand who
the guardians of the market are and their roles in protecting customers and enforcing rules. I also
place considerable emphasis on opening, closing, transferring, and handling customers’ accounts.
And, of course, I provide practice questions to guide you on your way. At the end, I give you a
30-question chapter quiz to help you test your knowledge.
Meeting the Market Watchdogs: Securities
Regulatory Organizations
To keep the market running smoothly and to make sure investors aren’t abused (at least too
much), regulatory organizations stay on the lookout. Although you don’t need to know all the
minute details about each of them, you do have to know the basics.
The Securities and Exchange Commission
The U.S. Securities  and Exchange Commission  (SEC) is  the maÛor watchdog of the securities
industry. Congress created the SEC to regulate securities markets and to protect investors from
Chapter 16
IN THIS CHAPTER
»Meeting the self-regulatory
organizations
»Opening and handling customer
accounts
»Playing by the rules
»Reviewing additional topics tested
»Checking your knowledge with a
chapter quiz
260 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
fraudulent and manipulative practices. All brokerɡdealers who transact business with investors
and other brokerɡdealers must register with the SEC. And that registration means something: All
brokerɡdealers have to comply with SEC rules or face censure (an official reprimand), limits on
activity, their own suspension or suspension of one or more associated persons (such as a regis-
tered rep or principal), a fine, and/or having their registration revoked.
SEC investigations may lead to a civil (financial) complaint being filed in a federal court. The SEC
may seek disgorgement (taking away) of ill-gotten gains, civil money penalties, and inÛunctive
relief (a cease-and-desist order from the court). If the matter is criminal in nature, the investiga-
tion is conducted by the U.S. attorney’s office and the grand Ûury.
Among its other numerous functions, you need to be aware that the SEC also enforces the follow-
ing acts:
»
The Securities Act of 1933: The Act of 33 reTuires the full and fair disclosure of all material
information about a new issue.
»
The Securities Exchange Act of 1934: The Act of 3, which established the SEC, was
enacted to protect investors by regulating the overthecounter (2TC) market and e[changes,
such as the 1ew <ork Stock E[change (1<SE). Chapter  tells you more about markets. In
addition, the Act of 3 regulates
•
The e[tension of credit in margin accounts (see Chapter 2)
•
The registration and regulation of brokers and dealers
•
The registration of securities associations
•
Transactions by insiders
•
Customer accounts
•
Trading activities
»
The Trust Indenture Act (TIA): This act, formerly called the Trust Indenture Act of 3,
prohibits bond issues valued at more than 0 million (originally  million) from being o΍ered
to investors without an indenture. The trust indenture is a written agreement that protects
investors by disclosing the particulars of the issue (the coupon rate, the maturity date, any
collateral backing the bond, and so on). As part of the Trust Indenture Act, all companies
must hire a trustee whoȇs responsible for protecting the rights of bondholders.
»
The Investment Company Act of 1940: This act regulates the registration reTuirements and
the activities of investment companies.
»
The Investment Advisers Act of 1940: This act reTuires the registration of certain investment
advisers with the SEC. An investment adviser is a person who receives a fee for giving invest
ment advice. Any investment adviser with at least 2 million of assets under management or
anyone who advises an investment company must register with the SEC. All other investment
advisers have to register on the state level. The Investment Advisers Act of 0 regulates
•
Recordkeeping responsibilities
•
Advisory contracts
•
Advertising rules
•
Custody of customersȇ assets and funds
CHAPTER 6  5ules and 5egulations 1o )ooling $round  261
Self-regulatory organizations
As you can imagine, due to the unscrupulous nature of some investors and registered representa-
tives, the SEC’s Ûob is overwhelming. Fortunately, a few self-regulatory organizations (SROs) are
there  to  take  some  of  the  burden  off  of  the  SEC’s  shoulders.  Although  membership  isn’t
mandatory, most brokerɡdealers are members of one or more SROs. SRO rules are usually stricter
than those of the SEC.
The four types of SROs you need to know for the SIE are the FINRA, MSRB, NYSE, and CBOE:
»
Financial Industry Regulatory Authority (FINRA): )I1RA is the SR2 responsible for the
operation and regulation of the 2TC market, investment banking (the underwriting of securi
ties), 1<SE trades, investment companies, limited partnerships, and so on. )I1RA was created
in 200 and is a consolidation of the 1ational Association of Securities 'ealers (1AS') and the
regulation and enforcement portions of the 1<SE. )I1RA is responsible for making sure that its
members follow not only )I1RA rules, but also the rules set forth by the SEC. Additionally, the
)I1RA is responsible for handling complaints against member ȴrms and may take disciplinary
action if necessary. )I1RA is also responsible for administering securities e[ams such as the
SIE. (1ow you know who to blame.) )I1RA has strict rules (as the other SR2s do, I suspect)
regarding ȴling of misleading, incomplete, or inaccurate information concerning membership,
the ȴrmȇs registration, and the registration of member associates.
»
Municipal Securities Rulemaking Board (MSRB): The 0SR% was established to develop rules
that banks and securities ȴrms have to follow when underwriting, selling, buying, and recom
mending municipal securities. (Check out Chapter  for info on municipal bonds.) The 0SR% is
subMect to SEC oversight but does not enforce SEC rules.
The 0SR% makes rules for ȴrms (and representatives) who sell municipal bonds but donȇt
enforce them it leaves enforcement up to )I1RA.
»
NYSE: The 1<SE is the oldest and largest stock e[change in the 8nited States. The 1<SE is
responsible for listing securities, setting e[change policies, and supervising the e[change and
member ȴrms. The 1<SE has the power to take disciplinary action against member ȴrms.
»
Chicago Board Options Exchange (CBOE): The C%2E is an e[change that makes and enforces
options e[change rules.
Although SROs may be independent, they work together creating and enforcing rules. FINRA and
NYSE can fine, suspend, censure (reprimand), and expel members; however, the FINRA and NYSE
can’t imprison members who violate the rules and regulations.
Look at SIE questions with the words guarantee or approve in them very carefully. The FINRA, SEC,
NYSE, and so on do not approve or guarantee securities. Any statement that says that they do is
false. In addition, because a firm is registered with (or didn’t have its registration revoked by) an
SRO, it does not mean that the SRO approves of the firm, its financial standing, its business, its
conduct, and so on. As such, member firms and their associates may not claim that they’ve been
approved by the SEC or any SRO.
State regulators
The North American Securities Administrators Association (NASAA) is devoted to investor protec-
tion. It is a voluntary association that consists of 67 regulators. NASAA even predates the creation
of the SEC. Its key roles include
»
/icensing stockbrokers, smaller investment adviser ȴrms (ones managing less than 00 million
in assets), and securities ȴrms conducting business in the state.
262 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
»
Registering securities on the state level.
»
Investigating customer complaints and possible cases of investment fraud.
»
Enforcing state securities laws. As such, the 1ASAA may ȴne, penali]e, provide restitution to
investors, assist in prosecuting investmentrelated criminals, and impose new conduct laws to
correct problems as they arise.
»
E[amining investment adviser ȴrms and brokerȂdealers to ensure compliance with securities
laws and making sure they keep accurate client records.
»
Reviewing o΍erings that are not e[empt from state law.
»
Providing education to investors regarding their rights and providing information so that they
can make more informed ȴnancial decisions.
»
Advocating for the passage of state securities laws.
When it comes to the SIE exam, don’t go crazy trying to remember every minute detail regarding
the NASAA; you’ll have to know more when taking the Series 63, Series 65, or Series 66. Get a
general feeling for what they do so that you’re able to recognize them in a question.
Department of the Treasury/IRS
The U.S. Department of the Treasury (USDT) was established to manage U.S. government reve-
nue. As such, the USDT oversees the printing of all paper currency and minting of all coins. In
addition, it is responsible for collecting taxes through the Internal Revenue Service (IRS); it is
responsible for managing U.S. government debt securities (T-bonds, T-notes, T-bills, and so on);
it licenses banks; and it helps advise U.S. government branches regarding fiscal policy.
FINRA Registration and Reporting
Requirements
Unless an individual is exempt from registration requirements, all brokerage firms have registra-
tion and reporting requirements that must be followed for their employees. Financial profession-
als must fill out U4 forms, be fingerprinted, pass necessary exams, take continuing education,
and so on.
Filling out the U4 form
Persons wanting to register as financial professionals with FINRA (like you) must submit a U4
form. The application includes things like a ten-year employment history and a five-year resi-
dential history; if you’re registered with another firm, how you’re registering (Securities Trader,
Financial and Operations Principal, General Securities Representative, and a slew more); states
you want to be registered in; and so on. In addition, applicants must submit their fingerprints.
All  U4  forms  (
www.finra.org/sites/default/files/form-u4.pdf)  must  be  thoroughly
reviewed by a principal of the firm. Background checks must be performed, and the applicant’s
employers for the previous three years must be called to verify the applicant’s employment his-
tory. The calls must be made within 30 days of the firm receiving the U4 form. Special scrutiny of
the applicant is required if the applicant has previously worked in the securities industry. Infor-
mation contained in the U4 form must be complete and not misleading.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  263
The U4 form also contains an arbitration disclosure, which states that disputes between the appli-
cant and the member firm will be settled by arbitration (essentially, you won’t take the firm
to court).
Although a lot of information listed here can disqualify a person, most of the information follows
a common theme —which makes sense; you shouldn’t have to memorize it all, in other words.
However, I suggest you be aware of the ten-year disqualification rule if an individual has been
convicted (not charged or accused) of a felony or certain misdemeanors. In addition, if a registrant
includes misleading information or omits information, their registration will be denied.
Note: Nonregistered (unregistered) persons may not solicit customers or take orders. In addition,
member firms are prohibited from paying commissions, fees, concessions, discounts, and so on
to any person who is not registered. The failure of a member firm to register someone who should
be registered will likely end in disciplinary action by FINRA. Nonregistered persons may handle
basic questions. (What is your location? Can I leave a message? What are your hours?) In addition,
they may send out literature, transfer calls, set up appointments, let customers know about
upcoming seminars, and such. They can’t be directly involved in securities business (opening
accounts, taking trade orders, soliciting trades, giving quotes, and so on). In the event that a
nonregistered person is to handle securities and/or money, they must be fingerprinted.
Missing the mark *rounds Ior disqualification
A  person  will  be sttĒtïriÞĤ ±isþĒÞifie±  from  membership  from  FINRA  under  the  following
circumstances:
»
If they had a felony criminal conviction or certain misdemeanor convictions within the last
ten years.
»
If they have had a temporary or permanent inMunction (no matter what the inMunctionȇs age)
issued by a court involving a long list of unlawful investment activities.
»
If they have been e[pelled, barred, or are currently suspended from membership or participa
tion in another selfregulatory organi]ation. This holds true even if the person has been barred
with the right to reapply.
»
If they have been barred or current suspension orders are coming from the SEC, Commodity
)utures Trading Commission (C)TC), or any other appropriate authority or regulatory agency.
As with the preceding rule, this holds true even if the person has been barred with the right to
reapply.
»
If they have been denied or had their registration revoked by the C)TC, SEC, or any other
appropriate authority or regulatory agency.
»
If it has been found that a member or person has made certain false statements in their
application, in reports, or in proceedings before the SEC, SR2s, or any other appropriate
regulatory authority or agency.
»
If any ȴnal order from a state securities commission (or from any agency or state oɝcer
performing similar functions), savings association, credit union, any state authority that
e[amines or supervises banks, state insurance commission (or any oɝce or agency perform
ing similar functions), an appropriate federal banking agency, or the 1ational Credit 8nion
Administration.
•
%ars said person from association with an entity (such as a brokerȂdealer, investment
advisory ȴrm, and so on) regulated by such commission, agency, authority, or oɝcer, or
from engaging in the business of banking, insurance, securities, savings association
activities, or credit union activities.
264 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
•
Constitutes a ȴnal order based on violations of any regulations or laws that prohibit
manipulative, fraudulent, or deceptive conduct.
»
If the SEC, C)TC, or any SR2 ȴnds that a person
•
Ȋ:illfullyȋ violated federal securities laws, Ȋwillfullyȋ violated commodities laws, or Ȋwillfullyȋ
violated 0SR% rules.
•
Ȋ:illfullyȋ aided, commanded, induced, abetted, counseled, or procured violations as set
forth in the preceding rule.
•
)ailed to supervise another person who committed violations as set forth in rule
number one.
+anding oYer your fingerprints
Under SEC Rule 17f-2 (you don’t have to remember the rule number), all employees of a broker-
age firm are required to be fingerprinted if they are involved in any of the following activities:
»
0aking sales
»
Handling assets (cash andor certiȴcates)
»
Accessing original books and records
»
Supervising any of the preceding activities
Fingerprints are always required when a person is applying for registration. The fingerprints
must  be  submitted  as  well  as  the  U4  form.  If  FINRA  doesn’t  receive  the  fingerprints  within
30 days of the U4 being submitted, the applicant’s registration will be deemed inactive.
The information you provide and your investment professional history don’t remain in a bubble.
The Central Registration Depository’s (CRD’s) BrokerCheck (
https://brokercheck.finra.org/)
allows investors access to vital information that they may need to help them pick the right firm
and the right professional, like you. Don’t worry; it won’t disclose your address, Social Security
number, and the like. However, it will disclose complaints against you and your employer, where
you and your employer are registered, exams you passed, how many years you’ve been in the
business, if you were convicted or pled guilty to a crime, if you or your broker have been expelled
from  an  SRO,  and  so  on.  If  a  member  maintains  a  website,  the  site  must  provide  a  link  to
BrokerCheck.
Continuing education
Yes, even after you’ve passed your securities exams like this one, you’re not done. You’re required
to take continuing education programs as required by FINRA. These are to make sure that you are
up-to-date with any new laws and that you remember the existing ones. Two elements of con-
tinuing education are required: the firm element and the regulatory element.
Firm element
Member firms must have annual meetings covering the services and strategies offered by the
firm. In addition, the meeting must cover any recent regulatory developments, if any. The meet-
ings must be interactive and allow people to ask questions. All registered persons who have direct
contact with the public must attend the meeting. All firms must have continuing and current
education programs for their covered employees.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  265
Regulatory element
All registered persons are required to take a computer-based training session covering FINRA
regulations by December 31st of each year. In the event that the training isn’t taken within the
required period, the person’s securities license(s) will be deactivated until it’s completed. If the
registered person’s licenses have been deactivated for two years, the individual will be adminis-
tratively terminated. If administratively terminated, the person must reapply for registration.
What happens when a rep resigns
or is terminated
If you leave your firm for whatever reason, the member firm you were working for has to file a U5
form with the CRD within 30 days of the date you resigned or were terminated. You will also
receive a copy for your records. The U5 form requires the member firm to provide an explanation
of why you left or why you were terminated. If you’re moving to a new member firm, your new
employer must file a new U4 form and receive a copy of the U5 filed by your former employer.
Things sometimes change, so if something on your U4 or U5 form is or becomes inaccurate, your
firm must update the information on the CRD. This could be something as simple as an address
change or something a tad more complex — a violation of some kind or (Heaven forbid) a felony
conviction.
Don’t wait too long going from one firm to another. After a U5 form has been filed on your behalf,
you have up to two years to get registered with another firm or you’ll have to take your securities
exams all over again. You certainly don’t want that to happen.
Skipping a step: Who’s exempt
from FINRA registration
Certain individuals who work for a member firm are exempt from FINRA registration. These
include
»
Persons whose functions are solely clerical or ministerial
»
Persons solely a΍ecting transactions on the ȵoor of a national securities e[change and who
are registered with that e[change
»
Persons whose function is solely and e[clusively involved in transactions of municipal
securities
»
Persons whose function is solely and e[clusively involved in transactions of commodities
»
Persons whose function is solely and e[clusively involved in transactions in securities futures,
as long as that person is registered with a registered futures association
Adhering to reporting requirements
Under  FINRA  Rule  4530,  member  firms  must  report  specified  events,  including  quarterly
statistical and summary information regarding customer complaints as well as copies of certain
civil  and  criminal  actions.  Members  must  report  promptly  (no  later  than  30  days  after  the
member knows or should’ve known about the event) if the member (or associated person of the
member)
266 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
»
Has been found to have violated any securitiesrelated or nonsecuritiesrelated investment
laws or standards of conduct by a 8.S. or foreign regulatory organi]ation.
»
Is the subMect of a written customer complaint involving allegations of theft or misappropria
tion of funds or securities.
»
Is the subMect of a written customer complaint involving allegations of forgery.
»
Has been named as a defendant or respondent in a proceeding brought by a 8.S. or foreign
regulatory body alleging a violation of rules.
»
Has been denied registration, suspended, e[pelled, or disciplined by a 8.S. or foreign regula
tory organi]ation.
»
Is indicted, convicted of, or pleads guilty to any felony or certain misdemeanors in or outside
the 8nited States.
The preceding list includes firm reporting requirements under Rule 4530, but firms are required
to report certain other events, too. These include
»
2utside business activities (covered in the following section).
»
Private securities transactions ȃ transactions outside the brokerȂdealerȇs normal business, in
other words. )or argumentȇs sake, say that an associate of a ȴrm has a client who wants to
trade options but their ȴrm doesnȇt trade options because it doesnȇt have an options principal.
In this case, with the permission of their ȴrm, they can accept the order from their client and
do the trade through another ȴrm.
»
Political contributions and conseTuences for e[ceeding dollar contribution thresholds (see
ȊAvoiding violationsȋ later in the chapter).
»
)elonies, ȴnancialrelated misdemeanors, liens, bankruptcies.
Outside business activities
While you’re building your business and getting new clients, you may feel the need to make a few
extra bucks working another Ûob. If so, you must notify your brokerage firm in writing. However,
you don’t need to receive written permission to work the other Ûob. Your member firm may reÛect
or restrict your outside work if it feels there is a conflict of interest. (Volunteering does not
require written notification.)
$ccounts at other ErokerȂdealers and financial institutions
Although  you  probably  won’t  do  this,  persons  associated  with  a  member  firm  may  open  an
account at another member firm (executing firm) with prior written permission from the employ-
ing firm. The associated person must also let the executing firm know that they are working for
another member firm. Duplicate confirmations and statements must be sent to the employing
firm if requested.
Private securities transactions
When involved in a private securities transaction, associated persons must provide written notice
to their employing firm. These take place when an associated person is involved in a securities
transaction outside of their normal business and outside of their employing member firm.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  267
If an associated person would like to enter into a private securities transaction, they must:
»
Provide written notice to their employing ȴrm
»
E[plain their role in the possible transaction
»
'escribe complete details of the possible transaction
»
'isclose whether they will receive compensation (what type andor dollar amount) for the
transaction
Whether the associated person receives compensation or not, the employing firm must provide
approval. Transactions for immediate family members in which the associated person does not
receive compensation are not considered private securities transactions.
Trading by the Book When
the Account Is Open
After you’ve opened a new account, you have to follow additional rules and regulations to keep
working in the business. You need to know how to receive trade instructions and how to fill out
an order ticket, as well as settlement and payment dates for different securities.
Filling out an order ticket
When you’re working as a registered rep, completing documents such as order tickets will become
second nature because you’ll have them in front of you. When you’re taking the SIE, you don’t
have that luxury, but you still need to know the particulars about what to fill out.
Getting the particulars on paper (or in binary form)
When your customer places an order, you have to fill out an order ticket. Order tickets may be on
paper or entered electronically, which happens more often. Regardless of how you enter the order,
it needs to contain the following information:
»
The registered repȇs identiȴcation number
»
The customerȇs account number
»
The description of the security (stocks, bonds, symbol, and so on)
»
The number of shares or bonds that are being purchased or sold
»
:hether the registered rep has discretionary authority over the account
»
:hether the customer is buying, selling long (selling securities that are owned), or selling short
(selling borrowed securities see Chapter 2)
»
)or option tickets, whether the customer is buying or writing (selling), is covered or uncovered,
and is opening or closing (see Chapter  for info on options)
»
:hether itȇs a market order, goodtillcanceled (*TC) order, day order, and so on
»
:hether the trade is e[ecuted in a cash or margin account
»
:hether the trade was solicited or unsolicited
268 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
»
The time of the order
»
The e[ecution price
Figure 16-1 shows you what standard paper order tickets may look like.
Designating unsolicited trades
Normally, you’ll be recommending securities in line with a customer’s investment obÛectives. If,
however, the customer requests a trade that you think is unsuitable, it’s your duty to inform them
about it. You don’t have to reÛect the order. (It’s the customer’s money to do with is they see fit
and, when all is said and done, you’re in the business to generate commissions.) If the customer
)Ζ*85E 1-1
%uy and sell
order tickets
have spaces
for the info
you need
to make a
trade.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  269
still wants to execute the trade, simply mark the order as unsolicited, which takes the responsibil-
ity off your shoulders.
$ trip to the principalȇs oɝce 6ecuring a signature
Principals are designated managers of a firm. All brokerage firms must have at least two principals
(unless the firm is a sole proprietorship). When you open or trade an account, you have to bring
the new account form or order ticket to a principal to sign. Principals need to approve all new
accounts, all trades in accounts, and all advertisements and sales literature; they also handle all
complaints (lucky break for you!), oversee employees, and watch for potential red flags. (Note: A
principal doesn’t have to approve a prospectus or your recommendations to your customers.)
Although you’ll generally bring an order ticket to a principal right after taking an order, the prin-
cipal can sign the order ticket later in the day. If you’re questioned about this on the SIE exam,
you want to answer that the principal needs to approve the trade on the same day, not before or
immediately after the trade.
Proportionate sharing
Members or associated persons are prohibited from sharing in the profits or losses in a custom-
er’s account. An exception to this rule is if the associated person contributed to the account. In
that case, the associated person needs a written authorization from the customer and principal
and the profits and/or losses are shared by the customer and associated member based on the
percentage contributed. Exempt from the rule of proportional sharing are accounts of immediate
family (parents, mother-in-law, father-in-law, spouse, or children) of the associated member.
Checking your calendar: Payment
and settlement dates
Securities that investors purchase have different payment and settlement dates. Here’s what you
need to know:
»
Trade date: The day the trade is e[ecuted. An investor who buys a security owns the security
as soon as the trade is e[ecuted, whether or not they have paid for the trade.
»
Settlement date: The day the issuer updates its records and the certiȴcates are delivered to
the buyerȇs brokerage ȴrm.
»
Payment date: The day the buyer of the securities must pay for the trade.
Unless the question specifically asks you to follow FINRA or NYSE rules (which I doubt it will),
assume the Fed regular  way settlement and payment dates as they appear in Table 16-1. The
FINRA and NYSE rules both require payment for securities to be made no later than the settlement
date, but the Federal Reserve Board states that the payment date for corporate securities is four
business days after the trade date.
Cash trades (which are same-day settlements) require payment for the securities and delivery of
the securities on the same day as the trade date.
In certain cases, securities may not be able to be delivered as in the preceding chart. In these
cases, the seller may specify that there’s going to be a delayed delivery. There can also be a mutually
agreed upon date in which the buyer and seller agree on a delayed delivery date prior to or at the
time of the transaction.
270 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
The when, as, and if issued (when-issued transaction) method of delivery is used for a securities issue
that has been authorized and sold to investors before the certificates are ready for delivery. This
method is typically used for stock splits, new issues of municipal bonds, and Treasury securities
(U.S. government securities). The settlement date for when-issued securities can be any of the
following:
»
A date to be assigned
»
Two business days after the securities are ready for delivery
»
2n the date determined by )I1RA
Safeguarding investor info: Regulation S-P
According to Regulation S-P, brokerɡdealers, investment companies, and investment advisers
must “adopt written policies and procedures that address administrative, technical, and physical
safeguards for the protection of customer records and information.” This means that members
must provide a way for securing customers’ nonpublic personal information, such as Social Secu-
rity numbers, bank account information, or any other personally identifiable financial informa-
tion. Members must provide customers a notice of their privacy policies. Members may disclose a
customer’s nonpublic information to unaffiliated third parties unless the customer opts out and
chooses not to have his information shared. A firm must include their policies to protect to the
security of a customer’s nonpublic information in their customer privacy and opt-out notices.
Members must make every effort to safeguard customers’ information, including securing com-
puters, encrypting emails, and so on.
&onfirming a trade
A tr±e «ïçfirmtiïç (receipt of trade) is the document you send to a customer after a trade has
taken place. You have to send out trade confirmations after each trade, at or before the completion
of  the  transaction  (the  settlement  date).  Here’s  a  list  of  information  included  in  the
confirmation:
»
The customerȇs account number
»
The registered repȇs I' number
»
The trade date
»
:hether the customer bought (%2T), sold (S/'), or sold short
»
A description of the security purchased or sold
»
The number of shares of stock or the par value of bonds purchased or sold
TABLE 1-1	Regular Way Settlement and Payment Dates
Type of Security
Settlement 'ate (in %usiness
'ays after the Trade 'ate)
Payment 'ate (in %usiness
'ays after the Trade 'ate)
Stocks and corporate
bonds
2 (T+2 ȃ two business days after
the trade date)
4
0unicipal bonds2 (T+2)2
8.S. government bonds (T+)
2ptions (T+)4
CHAPTER 6  5ules and 5egulations 1o )ooling $round  271
»
The yield (if bonds)
»
The Committee on 8niform Security Identiȴcation Procedures (C8SIP) number (a security I'
number, in other words)
»
The price of the security
»
The total amount paid or received, not including commission or any fees
»
The commission, which is added on purchases and subtracted on sales (if the brokerȂdealer
purchased for or sold from its own inventory, the markdown or markup doesnȇt have to be
disclosed)
»
The net amount, or the amount the customer paid or received after adding or subtracting the
commission (if the investor purchased or sold bonds, the accrued interest is added or
subtracted during this calculation)
»
:hether the trade was e[ecuted on a principal or agency basis (the capacity)
You should recognize the items listed in the preceding list, which are required for most securities
trades including municipal bonds. However, the MSRB tends to be a little stricter and also requires
the following information:
»
:hether the member acted as an agent for both the customer and another person for the
same trade
»
The time of e[ecution for institutional accounts or transactions in municipal fund securities
»
The settlement date
»
<ieldtomaturity or yieldtocall, whichever is lower
»
)inal monies, including the total dollar amount of the transaction and accrued interest if
applicable
»
:hether thereȇs any credit backing the securities (for revenue bonds, the source of revenue
or if thereȇs insurance backing the bonds)
»
Any special features of the bonds (callable, puttable, stepped coupon, book entry only,
and so on)
»
Information on the status of the securities (prerefunded, called, escrowed to maturity,
securities in default, and so on)
»
Ta[ information (ta[able, nonta[able, subMect to alternative minimum ta[, original issue
discount)
PHYSICAL VERSUS BOOK ENTRY
Although many years ago almost all delivery of stock certificates and debt securities (bonds) was in physi
cal form (meaning you actually received the certificate), most delivery and settlement now is in book
entry form. Even though you donȇt get to actually hold your ofttimes coollooking certificates, book entry
helps save money and makes trading much easier. :hen purchasing securities via book entry, you will
receive a receipt of trade, showing you own the securities but will not receive the actual certificates. A
record of your trading activity is kept on the financial institutionȇs books. :hen it comes time to sell the
securities, nothing has to be transferred it is Must changed on the institutionȇs books, and you receive con
firmation (receipt) of the trade.
272 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
Acting in your customers’ best interest
As part of your Ûob, your clients’ interest has to come before your own. So besides understanding
your clients’ needs, you need to follow and understand regulatory rules as well.
SEC Regulation BI (Best Interest) - Rule 15i-1
SEC Regulation BI was established recently to enhance the Securities Exchange Act of 1934. All
brokerɡdealers are required to act in the best interest of their customers. In that regard, brokerɡ
dealers are required to comply with the following rules:
»
Theyȇre reTuired to disclose all relationships with their clients in writing. This includes letting
clients know whether theyȇre acting as a broker or dealer in a trade, disclosing fees for
nontrade related services, the services they provide, and any potential conȵicts of interest.
»
They must provide a Form CRS (customer relationship survey) to each client prior to the initial
recommendation to that client.
»
They must use reasonable care, skill, and diligence when making recommendations to clients.
»
They must establish procedures to disclose potential conȵicts of interest to customers when
making recommendations.
»
They must establish procedures to enforce compliance with Regulation %I.
)inancial exploitation oI specified adults
With people living longer and the number of seniors increasing, FINRA recently created rules to
help curb or handle cases of financial exploitations of specified adults (seniors — natural persons
(living human being) aged 65 or older — and natural persons aged 18 or older who have mental
or physical impairments that render them unable to protect their own interests). For specified
adults, financial institutions must obtain the information of a trusted contact person whom they
can contact regarding unusual trading activity in the account.
FINRA defines the term fiçç«iÞ eģûÞïittiïç as
(A) Ȋthe wrongful or unauthori]ed taking, withholding, appropriation, or use of a Speciȴed Adultȇs
funds or securitiesȋ or
(B) Ȋany act or omission by a person, including through the use of a power of attorney, guardian
ship, or any other authority regarding a Speciȴed Adult toȋ
(a) Ȋobtain control, through deception, intimidation or undue inȵuence, over the Speciȴed
Adultȇs money, assets, or propertyȋ or
(b) Ȋconvert the Speciȴed Adultȇs money, assets or property.ȋ
In the event that a member believes that the financial exploitation of specified adults has or may
be taking place, Rule 2165 allows the member to place a temporary hold on the disbursement of
the specified adult’s funds or securities. If a temporary hold has been put in place, the member
has up to two business days to contact all parties involved in the transaction as well as the trusted
contact person (unless the member believes that they are involved in the exploitation) to describe
the reason(s) for the temporary hold. The hold typically lasts up to 15 business days, which may
be extended, while being reviewed.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  273
The SIE and other FINRA exams cover topics related to protecting seniors, including
»
)irmsȇ marketing and communications to investors age 6 and older
»
Information reTuired when opening an account for a senior
»
Any disclosures provided to senior investors
»
Complaints ȴled by senior investors as well as how the ȴrm handles the complaints
»
Supervision of registered reps as they communicate with senior investors
»
The suitability and types of securities marketed and sold to senior investors
»
The training of a ȴrmȇs representatives as to how they are to handle the accounts of
speciȴed adults
FINRA  recently  created  a  helpline  (844-57-HELPS)  for  seniors  to  provide  support  and
assistance.
Borrowing from or lending to
Registered persons associated with a member firm are prohibited from borrowing money from a
customer or lending money to a customer unless the member firm has written procedures allow-
ing borrowing and lending money between registered persons and customers and one of the fol-
lowing applies:
»
The customer is a member of the registered personȇs immediate family (spouse, mother,
father, motherinlaw, fatherinlaw, children).
»
The customer is a ȴnancial institution such as a bank that is in the business of providing credit,
ȴnancing, or loans.
»
The customer and the registered person are both registered under the same member ȴrm.
»
The customer and the registered person have a personal relationship outside the brokerȂ
customer relationship.
»
The customer and the registered person have a business relationship outside the brokerȂ
customer relationship.
This only works if the member firm allows borrowing from or lending to customers. The regis-
tered member would have to notify and get written approval from their firm prior to entering into
a buying or lending arrangement unless it’s not required in the firm’s written rules.
Following up with account statements
An account statement gives the customer information about their holdings in the account along
with the market value at the time the statement was issued. Customers are required under FINRA
rule 2231 to receive account statements quarterly (once every three months). The account state-
ment needs to include all account activity, securities positions, and money balances during the
period from the time the customer received the previous account statement. For mutual funds, no
matter how much (or little) trading was done, a customer needs to receive an account statement
semiannually (every six months).
274 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
Customers may want to know how their accounts are doing, and they may wonder about the
condition of the firm that they’re working with. So upon request by a customer, a member firm
must disclose its financial condition by delivering its most recent balance sheet (not income
statement). The balance sheet may be delivered in paper form or in electronic form (email) if the
customer agrees to the electronic delivery.
Keeping your dividend dates straight
When customers are purchasing securities of a company that’s in the process of declaring or pay-
ing a dividend, you need to be able to tell those customers whether they’re entitled to receive the
dividend. Because stock transactions settle in two business days, the customers are entitled to the
dividend if they purchase the securities at least three days prior to the record date. Here’s a list of
the four need-to-know dates for the SIE exam:
»
Declaration date: The day that the corporation oɝcially announces that a dividend will be
paid to shareholders. 2n the declaration date, the dividend amount, the record date, and the
payment date, will be announced.
»
Ex-dividend date (ex-date): The ȴrst day that the stock trades without dividends. An investor
purchasing the stock on the e[dividend date isnȇt entitled to receive the dividend because
stock transactions take two business days to settle, the e[dividend date is automatically one
business day before the record date.
The e[dividend date is the day that the price of the stock is reduced by the dividend amount.
(Chapter 6 tells you more about dividends and related calculations.) :hen a stock is purchased
e[dividend (on or after the e[dividend date), the seller is entitled to the dividend, not the
buyer. %ecause the dividend may not be paid for up to a month and sometimes longer, the
buyer is reTuired to sign a due bill indicating that the dividend belongs to the seller. In the case
of a cash dividend, the due bill is in the form of a due bill check, which is payable on the date
the dividend is paid by the issuer. In addition, if an investor buys a stock on time to receive a
dividend but for some reason will not receive the certiȴcates on time (by the record date), the
seller must send a due bill to the buyer. A due bill states that the buyer is entitled to the rights
of ownership even though theyȇve not yet received the certiȴcates.
»
Record date: The day the corporation inspects its records to see who gets the dividend. To
receive the dividend, the investor must be listed as a stockholder in company records.
»
Payment (payable) date: The day that the corporation pays the dividend to eligible
stockholders.
As you can see from the diagram, the buyer receives the dividend if they purchase the stock before
the ex-dividend date. If the stock is purchased on or after the ex-dividend date, the seller receives
the dividend.
To help you remember the sequence of dates, use the phrase Don’t Eat Rubber Pickles. I know it
sounds ridiculous, but the more ridiculous, the easier it is to remember.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  275
The board of directors must announce three dates: the declaration date, the record date, and the
payment date. The ex-dividend date doesn’t need to be announced because it’s automatically one
business day before the record date. However, mutual funds have to announce all four dates
because they may set their ex-dividend date at any time (even on the record date).
The following question tests your ability to answer a dividend question.
Wedgie Corporation has Ûust announced a 50-cent cash dividend. If the record date is Tuesday,
March 9, when is the last day an investor can purchase the stock and receive the dividend?
(A) March 4
(B) March 5
(C) March 7
(D) March 8
The  answer  you’re  looking  for  is  (B).  For  an  investor  to  purchase  the  stock  and  receive  a
previously declared dividend, they must purchase the stock at least one business day before the
ex-dividend date. This question is a little more difficult because you have a weekend to take into
consideration.
The ex-dividend date is March 8, which is one business day prior to the record date. This investor
has to buy the stock before the ex-dividend date in order to receive the dividend, so they have to
buy it March 5 or before (because the 6th and 7th are Saturday and Sunday). The last day an
investor can purchase the stock and receive the dividend is March 5.
If a stock is sold short (if the investor is selling a borrowed security), the lender of the stock sold
short is entitled to receive the dividend. (See Chapter 9 for details on margin accounts.) Also, the
trades in the example problems are regular way settlement (three business days after the trade
date); remember that cash transactions settle on the same day as the trade date. In the case of
dividends, if an investor purchases stock for cash, they receive the dividend if they purchase the
stock anytime up to and including the record date.
Handling complaints
It’s bound to happen sooner or later, no matter how awesome you are as a registered rep: One of
your customers is going to complain about something (like unauthorized trades, guarantees, and
so on). Complaints aren’t considered official unless they’re in writing. If necessary, FINRA wants
you to follow the proper procedure for handling complaints. The following sections cover formal
and informal proceedings.
276 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
Code of procedure (COP)
The code  of  procedure is FINRA’s formal procedure for handling securities-related complaints
between public customers and members of the securities industry (brokerɡdealers, registered
reps, clearing corporations, and so on). The public customer has the choice of resolving the com-
plaint via the formal code of procedure or the informal code of arbitration. (See the next section.)
All complaints going through code of procedure must be responded to by the firm within 25 days
after receipt of the customer complaint.
In the code of procedure, the FINRAs’s Department of Enforcement (DOE) is responsible for
investigating suspected violations. In the event that the investigation leads to what the DOE
believes is a violation, the DOE will hold a hearing. If the customer or member isn’t satisfied with
the results, they can appeal the decision to the FINRA board of governors. Decisions are appeal-
able all the way to federal appellate courts.
Code of arbitration
The code of arbitration is an informal hearing (heard by neutral arbiter or a panel of arbiters) that’s
primarily conducted for disputes between members of the FINRA. Members include not only
brokerɡdealers but also individuals working for member firms.
If you (a registered rep) have a dispute with the brokerɡdealer that you’re working for, you can
take the brokerɡdealer to arbitration. If a customer has a complaint against a brokerɡdealer or
registered rep, the customer has the choice of going through code of procedure (see the preceding
section) or code of arbitration, unless the customer has given prior written consent (usually by
way of the new account form) stating that they will settle disputes only through arbitration.
The decisions in arbitration are binding and nonappealable, so they’re less costly than court
action. If a member firm or person associated with that member firm fails to comply with the
terms of the arbitration (in the case of a loss) within 15 days of notification, FINRA reserves the
right to suspend or cancel the firm’s or person’s membership.
Mediation
If an investor and/or brokerɡdealer are looking for a more informal way to handle disputes, they
may voluntarily decide to go to mediation. Disputes settled through mediation are heard by an
independent third party. Unlike arbitration, mediation is nonbinding.
Not all complaints end up going to arbitration, to mediation, or go through the code of procedure.
Sometimes, the complaints are the result of miscommunication, such as instances in which the
customer made a mistake, a customer feels they were charged too much commission, and so on.
A lot of these complaints can be handled internally without the need for progression. However, all
complaints need to be kept on file along with any action taken.
Disseminating info: Appropriate
communications
To help promote their business and to keep customers up-to-date, member firms continually
send out sales literature, publish ads, run commercials, send out research reports, have scripted
seminars, and so on. As you can imagine, ads and such cannot omit material facts, exaggerate, or
be fraudulent or misleading, and must also explain the potential risks along with the potential
benefits. You’ve probably heard the disclaimers “Past performance does not indicate future per-
formance” and “People can and do lose money” in radio ads. Believe me, they wouldn’t put those
in unless they had to.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  277
FINRA divides communication into three categories:
»
Correspondence: Any written communication (including electronic) distributed or made
available to 25 or fewer retail investors (ones that are not institutional investors) within a
30calendarday period.
»
Retail communication: Similar to correspondence (see the preceding bullet) but made
available to more than 25 retail investors within a 30calendarday period.
»
Institutional communication: Any written communication (including electronic) distributed
or made available only to institutional investors, but not including a memberȇs internal
communications. Institutional investors include government entities, member ȴrms and
registered persons, employee beneȴt plans, a person acting solely on behalf of any such
institutional investor, and so on.
As with Ûust about everything that happens at a brokerage firm, retail communications must be
approved by a qualified principal of the firm. Research reports on particular securities must be
approved by a supervisory analyst who has expertise in the particular product. Testimonials (if
any) must be made by a person who has the knowledge and experience to have a valid opinion.
Member firms are in many cases required to file retail communications with FINRA ten business
days prior to first use. Members are required to keep the communications for a minimum of
three years.
Keeping clear records
As you can imagine, member firms must keep certain records on file. Depending on which records
they are, there are certain SEC retention requirements. The records do not necessarily need to be
kept in printed format; they can be kept digitally as long as they are in a nonerasable format.
Corporate or partnership documents of the member firm must be kept for the lifetime of the firm.
The documents must contain the list of officers, partners, and/or directors of the firm. Addition-
ally, U4 forms of all active employees must be kept as long as the firm is in business.
The following records must be kept for a minimum of siģ ĤersȽ
»
Blotters: %lotters are records of original entry relating to the purchase and sale of securities,
the receipt and deliver of securities, as well as the records of receiving or delivering cash.
»
Ledgers: Customer account statements, which include trade settlement dates.
»
General ledgers: A ȴrmȇs ȴnancial statements, which must be updated monthly. A general
ledger includes the ȴrmȇs assets, liabilities, and net worth.
»
Position record: A record of all the securities owned by the ȴrm and its location.
»
Account record: Terms and conditions of margin accounts and cash accounts.
»
Closed accounts: Records of customers whoȇve closed accounts.
Note: Like FINRA rules, MSRB rules require blotters, ledgers, closed accounts, and position records
to be kept for six years. However, MSRB also requires records relating to the underwriting of
municipal securities, complaints (FINRA, four years), supervisory records, and gift records to be
kept for six years.
278 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
The following records must be kept for a minimum of tÊree ĤersȽ
»
8 forms, 8 forms, and ȴngerprints of former employees
»
Trade conȴrmations
»
2rder tickets
»
Advertisements
»
Sales literature
»
'ividends and interest received in each account
»
Powers of attorney
»
Speechespublic appearances
»
Compliance procedure manuals
»
*ifts
»
Compensation records of associates
Note: MSRB rules require members to maintain certain records for four years. These include sub-
sidiary ledgers, trades, confirmations, terms and conditions of customer accounts, checkbooks
and canceled checks, delivery of official statements, public communications, and so on.
Whether the records have to be kept for three years, six years, or whatever, they have to be easily
accessible for two years (FINRA and MSRB).
As you can imagine, strict penalties are enforced for falsification, improper maintenance, or
improper  retention  of  records.  FINRA  reserves  the  right  to  inspect  the  books,  records,  and
accounts of all member firms and their associates. All regulatory requests by FINRA for specified
books, records, or accounts should be supplied by the member firm promptly.
Committing Other Important Rules to Memory
Brokers and investors must follow numerous rules to keep themselves from facing fines or worse.
In this section, I list a few of the more important rules.
Sticking to the 5 percent markup policy
The 5 percent policy (FINRA 5 Percent Markup Policy) is more of a guideline than a rule. The
policy was enacted to make sure that investors receive fair treatment and aren’t charged exces-
sively for brokerɡdealer services in the OTC market. The guideline says that brokerage firms
shouldn’t charge commissions, markups, or markdowns of more than 5 percent for standard
trades.
The following trades are subÛect to the 5 percent markup policy:
»
Principal (dealer) transactions: A ȴrm buys securities for (or sells securities from) its own
inventory and charges a markdown or markup.
»
Agency (broker) transactions: A ȴrm acts as a middleman (broker) and charges a
commission.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  279
»
Riskless (simultaneous) transactions: A ȴrm buys a security for its own inventory for
immediate resale to the customer (riskless to the ȴrm).
»
Proceeds transactions: A ȴrm sells a security and uses the money to immediately buy
another security. <ou must treat this transaction as one trade. (<ou canȇt charge on the way
out and on the way in.)
The 5 percent markup policy covers ïĝerɔtÊeɔ«ïĒçter tr±es ïÂ ïĒtstç±içÄȾ çïçeģemût se«Ērities ĞitÊ
public customers. If securities are exempt from SEC registration or if they’re new securities that
require a prospectus, they’re exempt from the 5 percent policy. Additionally, if a dealer pays
$20 per share to have a security in inventory (dealer cost), and the market price is $8 per share,
the dealer can’t charge customers $20 per share so that it doesn’t take a loss.
Under extenuating circumstances, the brokerage firm may charge more. Eustifiable reasons for
charging more (or less) than 5 percent include
»
E[periencing diɝculty buying or selling the security because the market price is too
low or too high.
»
Handling a small trade. If a customer were to place an order for 00 worth of securities, youȇd
lose your shirt if you were to charge only  percent () in this case, you wouldnȇt be out of line
if you were to charge 00 percent. %y the same token, if a customer were to purchase 
million worth of securities,  percent (0,000) would be considered e[cessive.
»
Encountering diɝculty locating and purchasing a speciȴc security.
»
Trading nonliTuid securities.
»
E[ecuting transactions on foreign markets.
Note: The 5 percent markup policy is a guideline that member firms should use when making
trades. However, firms may also charge customers for services performed other than trading
securities. These services include collection of monies due for principal, interest, or dividends.
They may also charge for the exchange or transfer of securities or the safekeeping of customers’
securities. The main thing for you to remember is that the charges should be reasonable and not
unfairly discriminatory.
Avoiding violations
It’s up to your firm and you to understand violations and avoid them. FINRA expects its members
and their representatives to “observe high standards of commercial honor and Ûust and equitable
principles of trade.”
You need to be aware of some violations not only for the SIE exam but also so you stay out of trou-
ble. Of course, the entire book and this chapter are filled with rules and violations. However,
some violations can be summed up in a sentence or two (or three); that’s what this section is for.
Some of the violations are more connected with brokerɡdealers, some with registered reps, and some
with investment advisers. Violators are subÛect to sanctions such as fines, censures, suspensions,
expulsions, and so on.
»
Commingling of funds: Combining a customerȇs fully paid and margined securities or
combining a ȴrmȇs securities with customer securities
»
Interpositioning: Having two securities dealers act as agents for the same trade so that two
commissions are earned on one trade
280 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
»
Giving (or receiving) gifts: *iving or receiving a gift of more than 00 per customer per year.
1oncash business e[penses (lunch, dinner, hotel rooms, travel e[penses, occasional tickets to
a sporting event, and so on) are e[empt from this rule.
»
Making political contributions (paying to play): 8nder the Investment Advisers Act of 0,
investment advisers are prohibited from providing investment advisory services for a fee to a
government client for two years after a contribution is made. This rule applies not only to the
adviser, e[ecutives, and employees making contributions to certain elected oɝcials, but also
to candidates who may later be elected. In addition, investment advisers are prohibited from
soliciting contributions for elected oɝcials or candidates if the investment adviser is seeking or
providing government business.
»
Falsifying or withholding documents: )irms cannot make up information or withhold
needed documents from customers or any SR2.
»
Signatures of convenience: %asically, forging a customerȇs signature even if approved by the
customer is a violation.
»
Guarantees: 0embers and associates are prohibited from making guarantees against loss in
any securities transaction or in any securities account of a customer.
»
Improper use: 0embers and associates are prohibited from making improper use of a
customerȇs securities or funds.
»
Freeriding: Allowing a customer to buy and then sell the same securities without paying for
the purchase. 8nder Regulation T, if a customer purchases and sells the same security in a
cash account without paying for the security, their account will be restricted for 0 days. )or
that 0day period, the customer will have to pay in full before purchasing securities.
»
Backing away: )ailure on the part of a securities dealer to honor a ȴrm Tuote.
»
Churning: A violation whereby a registered rep e[cessively trades a customerȇs account for the
sole purpose of generating commission.
»
Use of manipulative, deceptive, or other fraudulent devices: 0embers are prohibited
from inducing the sale or purchase of any security by means of manipulation, deception, or
any other fraudulent device or contrivance.
»
Trading ahead of research reports: 1o member shall trade a security based on information
received from a research report prior to that research report being released publicly.
»
Trading ahead of customer orders: 0embers are prohibited from placing their order ahead
of a customerȇs order. Their Mob is to get their customer the best price, and placing their order
ahead of the customerȇs will likely cause the customer to get a worse price.
»
1ot disclosing a financial relationship with the issuer It is a violation to not disclose if your
ȴrm has a ȴnancial relationship with the issuer, where finanFial relationsKiS is deȴned as being
controlled by, having a controlling interest in, or being under common control with the issuer.
In the event that there is a ȴnancial relationship, it must be disclosed (given to or sent to) the
customer prior to the completion of the transaction.
»
Frontrunning: A violation in which a registered rep e[ecutes a trade for themselves, their ȴrm,
or a discretionary account based on knowledge of a block trade (0,000 shares or more)
before the trade is reported on the ticker tape.
»
Prearranging trades: A prearranged trade is an illegal agreement between a registered rep
and a customer to buy back a security at a ȴ[ed price.
»
Paying for referrals: 0embers or persons associated with a member (for e[ample, registered
reps) are prohibited from paying cash or noncash compensation to any person e[cept those
registered with the member ȴrm or other )I1RA members. A violation occurs in the event that
compensation is paid to a nonmember for locating, introducing, or referring a client.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  281
Some violations include some sort of market manipulation. These include
»
Market rumors: 0embers are prohibited from spreading false market rumors that may
prompt others to either buy or sell a security.
»
Pump and dump: This is fake news that most often happens with penny stocks. In this case,
the promoters send out mass emails or regular mail to paint a glowing report on a particular
security, thus pumping it up. %ecause of the positive reports, many investors purchase the
security and drive the price up. At that point, the promoters sell (dump) their shares for a
nice proȴt.
»
Excessive trading: A violation whereby a trader places both buy and sell orders on the same
security around the same time, thus making it look like thereȇs a lot of trading activity on that
security.
»
Marking the open/marking the close: E[ecuting a series of trades within minutes of the
open or close to manipulate the price of a security.
»
Matching orders: Illegally manipulating the price of a security to make the trading volume
appear larger than it really is, such as two brokerage ȴrms working in concert by trading the
same security back and forth.
»
Painting the tape: Creating the illusion of trading activity due to misleading reports on the
consolidated tape, such as reporting a trade of 0,000 shares of stock as two separate trades
for ,000 shares each.
»
Paying the media: A violation in which brokerage ȴrms or aɝliated persons pay an employee
of the media (website, newspaper, maga]ine, radio, T9 show, and so on) to a΍ect the price of a
security, such as paying a T9 stock e[pert to recommend a security that the ȴrm has in its
inventory.
»
Anti-intimidation/Coordination: 0embers may not intimidate (threaten, harass, coerce, and
so on) other members into changing their price(s) on a security. In addition, a member may
not coordinate with another member to adMust the price of a security.
It is also considered a violation for a member firm to distribute cash or noncash compensation to
the employees of another member firm regarding the sale and distribution of securities unless all
of the following apply:
»
The compensation is not conditional on sales by the other ȴrm.
»
It has prior approval from the other member ȴrm.
»
The total amount of compensation does not e[ceed the limit of 00 per year.
Noncash compensation could be season tickets for the Eets, sending someone on vacation, gift
certificates, and so on. Providing an occasional meal, ticket to a sporting event, and such are con-
sidered acceptable business entertainment expenses as long as they’re neither too expensive nor
too frequent. And certain noncash expenses are considered okay as long as they’re business-
related — paying for a business dinner, paying for a seminar, providing airline tickets, and so on.
In addition, you don’t have to keep track of things that provide advertising, such as pens with
your name on them, coffee mugs with your picture, and so on.
Also, FINRA wants to make sure that members and their associates are making recommendations
based on their belief that they fall in line with their customer’s investment strategy and their
belief that the product(s) recommended is/are the right one(s). So to curb potential conflict of
interest, similar cash and noncash compensation rules are put in place for program sponsors,
such as investment companies. FINRA Ûust wants to make sure that recommendations are not
based on the fact that members or their associates owe someone.
282 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
Following the money: Anti-money-
laundering rules
The Bank  Secrecy  Act  establishes  the  U.S.  Treasury  Department  as  the  regulator  for  anti-
money-laundering  (AML)  programs.  All  brokerɡdealers  are  required  to  develop  programs  to
detect possible money-laundering abuses. In addition, all brokerɡdealers must review the Office
of Foreign Asset Control’s (OFAC) Specially Designated Nationals (SDN) list to make sure that
they’re not doing business with individuals or organizations that are on the list. Anti-money-
laundering programs are designed to help prevent dirty money that has been cleaned (made to
look like it came from a legitimate source) from being used to fund terrorist activities, illegal
arms sales, drug trafficking, and so on. Here are three stages of money laundering that you must
be aware of for the SIE exam (please, don’t try this at home):
1. Placement
In this initial stage of money laundering, the funds, derived from criminal activity, are trans
ferred into the ȴnancial system (typically via banks and brokerȂdealers).
2. Layering
/ayering is the money laundererȇs attempt to disguise the source of the funds, usually by
moving the funds from one place to another through a series of transactions.
3. Integration
Integration is the ȴnal stage of money laundering, when illegal funds are mi[ed (commingled)
with legitimate funds. /aunderers usually accomplish this step through businesses that operate
using cash, importing and e[porting companies, and so on.
Brokerɡdealers and other financial institutions must report any cash deposits, withdrawals, or
transfers of more than $10,000 in a single day through a Currency Transaction Report (CTR) to
FinCEN  (the  U.S.  Treasury  Financial  Crimes  Network).  An  institution  must  report  suspicious
activity  of $5,000  or  more  of  any  type  of  transaction  to  FinCEN  by  filing  a  Suspicious  Activity
Report (SAR).
Here are some indications of money laundering at the opening of the account:
»
Concern with 8.S. government reporting reTuirements
»
Reluctance to reveal information about business activities
»
Suspect I' such as a license or passport that looks like it was made in someoneȇs basement
»
Irrational transactions that are inconsistent with obMectives
»
A ȴduciary (the person who can legally make decisions for another investor) whoȇs reluctant
to provide information about the customer
»
An individualȇs lack of general knowledge of their industry
And here are some shady signals to look out for after the account is open:
»
Irregularly making deposits of large amounts of cash or money orders
»
Structuring ȃ making cash or casheTuivalent deposits (such as money orders) of Must under
0,000 to avoid having them be reported to the 8.S. government
»
0aking wire transfers to noncooperative countries (Iran, 1orth .orea, 1igeria, and so on)
who do not work with the 8S to try to curb money laundering
»
Engaging in sudden and une[plained wire activity
CHAPTER 6  5ules and 5egulations 1o )ooling $round  283
»
0aking a deposit and transferring it to another party without any business purpose
»
%uying a longterm investment and liTuidating it in the short term
»
0aking transfers between multiple accounts for no apparent reason
»
'epositing bearer bonds and reTuesting the money immediately
»
'isplaying a total lack of concern about risks and commissions
The signs of money laundering tend to make sense, so when answering an SIE exam question
about money laundering, think to yourself, “If it looks like a duck and quacks like a duck, it’s
probably a duck” — or in financial terms, “If it looks and seems like money laundering, it’s prob-
ably money laundering.”
Complying with AML rules
Under  the Bank  Secrecy  Act,  which  is  enforced  by  FinCEN,  all  financial  institutions,  including
brokerɡdealers,  must  develop  and  carry  out  anti-money-laundering  (AML)  programs.  These
programs must be approved in writing by a firm’s senior management. Financial institutions and
brokerɡdealers must do the following:
»
Initiate and carry out policies and procedures designed to detect and report suspicious
transactions
»
Initiate and carry out policies, procedures, and internal controls that are designed to comply
with the %ank Secrecy Actȇs regulations
»
Set up annual independent testing to make sure that the ȴrm is complying with the A0/ rules
under the %ank Secrecy Act
»
Appoint and indicate to )I1RA (by name, title, email address, phone number, and so on) the
person (a designated $0/ FomSlianFe oɝFer) or people responsible for implementing and
overseeing the daily internal controls of its A0/ program
AML programs are not necessarily static and are subÛect to change. Each firm is responsible for
making sure that its AML programs remain current.
Working with public info: Following
insider trading rules
Insider trading is a violation that occurs when an individual trades a particular publicly traded
security based on information that has not been released (or adequately released) to the public
(known as material nonpublic information). According to the Insider Trading and Securities Fraud
Enforcement Act of 1988, both the tipper (the one who shared the nonpublic information) and the
tippee (the one who traded based on the tip) are liable.
There is no violation of insider trading rules unless a trade takes place based on that inside infor-
mation. If a registered rep or anyone working at a firm receives what they believe to be inside
information, they should immediately report it to a principal of the firm.
Charges of insider trading have been brought against
»
2ɝcers, directors, and employees of a corporation who traded the corporationȇs securities
after learning of important, conȴdential corporate developments
284 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
»
)amily members, friends, business associates, and other people (tippees) who received tips
from the oɝcers, directors, and employees who traded the corporate securities based on
conȴdential information received
»
*overnment employees who traded based on conȴdential information received because of
their employment with the government, which has not (or not yet) been released to the public
»
Employees of brokerage, banking, law, and printing ȴrms who e[ecuted trades based on
conȴdential information received as part of their Mob
»
Political consultants who have given tips or traded based on material nonpublic information
they received from government employees
»
2ther persons who have taken advantage of or traded on conȴdential information they
received from employers, friends, family, and others
Putting it in simple terms, material nonpublic (inside) information is information that could
affect the market value of a security but the information has not been released (or adequately
released) to the public.
Penalties for insider trading
As you can imagine, the penalties for insider trading are pretty severe:
»
The ma[imum criminal ȴne for an individual is  million per violation and 2 million per
business per violation.
»
The ma[imum prison sentence is 20 years per violation.
»
The ma[imum civil sanctions are three times the gain or three times the loss avoided plus
disgorgement of proȴts.
Contemporaneous traders
Persons who enter orders at or about the same time as the person trading on inside information
on the opposite side of the market are called contemporaneous traders. So, for argument’s sake,
if the person with inside information sold shares of ABC common stock due to inside information,
a contemporaneous trader would be one who bought shares of ABC common stock at or about the
same time (and vice versa). In this case, the contemporaneous trader may actually sue the person
who  violated  the  insider  trading  rules.  The  suits  may  be  initiated  up  to  five  years  after  the
occurrence.
The Investor’s Bankruptcy Shield:
FDIC and SIPC Coverage
The Federal Deposit Insurance Corporation (FDIC) provides deposit insurance, which guarantees
a certain level of safety to people who have money on deposit at a bank. FDIC protects accounts
from bank failure (bankruptcy). At the present time, each depositor is protected up to $250,000.
The Securities Investor Protection Corporation (SIPC), which was created under the Securities
Investor  Protection  Act  of  1970,  protects  the  customer  against  brokerɡdealer  bankruptcy.
Although it’s not a government agency, this private, nonprofit organization was created by the
CHAPTER 6  5ules and 5egulations 1o )ooling $round  285
government in 1970. The SIPC protects each separate customer’s assets (securities and cash) up
to $500,000 total, of which no more than $250,000 can be cash.
Although brokerage firms are required to follow net capital rules — specifically, SEC Rule 15c3-1 —
that are designed to minimize the chances of brokerɡdealer failure and protect customer assets,
brokerɡdealers occasionally (too often) declare bankruptcy.
All members must advise clients at the opening of the account about SIPC protection and must
provide an SIPC brochure and info on contacting SIPC, including the SIPC’s web address and tele-
phone number. In addition, clients must receive all that same info in writing at least once a year.
The following question concerns SIPC coverage.
Steve Fredericks has a cash account with $150,000 in securities and $300,000 cash and a margin
account with $50,000 in equity. Additionally, Steve has a Ûoint cash account with his wife
Melissa with $250,000 in securities and $300,000 cash. If Steve’s brokerɡdealer goes bankrupt,
what is his coverage under SIPC?
(A) $450,000
(B) $500,000
(C) $850,000
(D) $950,000
The right choice is (D). If one of your customers has a cash and margin account titled under one
name, as Steve does, it’s treated as though it belongs to one customer. Therefore, Steve’s cash
and margin account is covered up to $500,000, of which no more than $250,000 can be cash. He’s
covered  for  the  $200,000  in  securities  ($150,000  in  securities  plus  the  $50,000  equity)  and
$250,000 of the $300,000 cash for a total of $450,000. Next, the Ûoint account with his wife is
treated as though from a separate customer. Therefore, that account is covered for the $250,000 in
securities and $250,000 in cash. Add the two together, and you see that Steve is covered for a total
of $950,000 ($450,000 plus $500,000).
If an investor is not fully covered under SIPC, the investor is still owed money by the bankrupt
brokerɡdealer; therefore, the investor becomes a general creditor of the firm for the balance owed.
Holding a customer’s mail
If one of your customers is not receiving mail at their usual address because they are traveling,
moving, or whatever, your firm can hold their mail for a specified time period up to three months
(or longer if for safety or security concerns). This typically has to do with confirmations and
account statements that the firm would normally mail. The member firm must have a way to
contact the customer in a timely manner (by phone, email, and so on), and the firm must provide
a way for the customer to receive information regarding their account (typically via email or
through the member’s website). In addition, the member firm must verify at reasonable intervals
that the customer’s instructions still apply.
Business continuity plans and emergency
contact information
FINRA requires that all member firms must set up and maintain business continuity plans (BCP)
to deal with the possibility of a business disruption. The idea is to make sure that customers will
still  be  able  to  contact  the  firm  and  be  able  to  access  their  securities  and  funds  during  an
286 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
emergency. Although the plan is somewhat flexible depending on the member’s business, some
of the items the plan should address include the following:
»
Hard copy and electronic data backup and recovery
»
Alternative communications between customers and members
»
Alternative communications between members and their employees
»
Alternative physical locations of employees
»
Regulatory reporting
»
Communication with regulators
»
How the member ȴrm will ensure that customers will be able to have prompt access to their
securities and funds in the event that the member is unable to continue business
A few other things could be on this list such as “all mission-critical systems” (ways they would
be able to handle customers’ orders and such), “financial and operational assessments” (how a
member’s operations would change), and so on. However, the preceding list should be able to get
you through SIE exam questions related to what needs to be on a firm’s business continuity plan.
Members are required to have a member of senior management (who must be a principal) approve
of their business continuity plan. That member is also responsible for conducting an annual
review. The member’s plan must be disclosed to customers in writing at the opening of their
account, posted on the firm’s website (if any), and mailed to customers upon request. In addition,
besides providing the plan info to FINRA, they must also provide emergency contact information
to FINRA. (FINRA must receive the names of two principals and members of senior management
to contact in the event of an emergency; if the contact info changes, it must be updated within
30 days.) In the event that any info changes regarding the business continuity plan, the firm is
responsible for updating its customers, employees, and FINRA.
Testing Your Knowledge
This chapter was Ûam-packed full of rules. Unfortunately, there wasn’t too much I could do about
that except to make them as easy to understand as possible. As you can imagine, because of the
size of this chapter, I’ve given you the most chapter questions . . . oh, Ûoy. Good luck!
Practice questions
1. Which of the following need to be included on a stock order ticket?
I. The customer’s signature
II. The time of the order
III. The number of shares
IV. Whether the trade is solicited or unsolicited
(A) I, II, and III
(B) II and III
(C) II, III, and IV
(D) I, II, III, and IV
CHAPTER 6  5ules and 5egulations 1o )ooling $round  287
2.
All of the following are self-regulatory organizations ECEPT
(A) NYSE
(B) SEC
(C) MSRB
(D) FINRA
3. Declan Smith has an account at Ayla Brokerɡdealer. Declan has not traded any securities at Ayla
Brokerɡdealer for over three years. How often is Ayla Brokerɡdealer required to send an account
statement to Declan?
(A) Monthly
(B) Quarterly
(C) Semiannually
(D) Annually
4. The ex-dividend date is ɗɗɗɗɗɗɗ business day(s) before the record date.
(A) one
(B) two
(C) three
(D) five
5. Which of the following is a violation that includes a form of market manipulation?
(A) Commingling
(B) Frontrunning
(C) Pump and dump
(D) Interpositioning
6. Which of the following are subÛect to the FINRA 5 percent markup policy?
I. Principal transactions
II. Agency transactions
III. Riskless transactions
IV. Proceeds transactions
(A) I and III
(B) II, III, and IV
(C) I, III, and IV
(D) I, II, III, and IV
7. Which of the following is an indication of money laundering when a customer opens an
account?
(A) Concern with U.S. government reporting requirements
(B) Reluctance to reveal information about business activities
(C) Questionable ID
(D) All of the above
288 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
8. A person will be statutorily disqualified from membership from FINRA under which of the
following circumstances?
I. If they had a felony conviction within the last 15 years
II. If they have been barred from membership in an SRO
III. If they have made false statements on their application
(A) I and III
(B) II and III
(C) I and II
(D) I, II, and III
9. If you resign from a brokerage firm, how long do you have to register with another firm so that
you don’t have to take your securities exams again?
(A) 90 days
(B) 6 months
(C) 1 year
(D) 2 years
10. Which of the following are violations?
(A) Commingling of funds
(B) Interpositioning
(C) Signatures of convenience
(D) All of the above
11. Which of the following securities transactions settle in two business days after the trade date?
I. Stock and corporate bond transactions
II. Municipal bond transactions
III. U.S. government bond transactions
IV. Option transactions
(A) I, III, and IV
(B) II and III
(C) I and II
(D) I, II, III, and IV
12. Brokerɡdealers, investment companies, and investment advisers must have written policies
designed to protect customers’ records and information. This rule falls under
(A) Regulation S-P
(B) Regulation D
(C) Regulation M
(D) Regulation T
13. All of the following must be included on a trade confirmation ECEPT
(A) a description of the security
(B) the markup or markdown
(C) the registered rep’s ID number
(D) the commission
CHAPTER 6  5ules and 5egulations 1o )ooling $round  289
14.
imbot Corporation has Ûust announced a 30-cent dividend to shareholders of record. If the
record date is Friday, October 8, when is the first day an investor can purchase the stock
and not receive the dividend?
(A) Wednesday, October 6
(B) Thursday, October 7
(C) Friday, October 8
(D) Monday, October 11
15. In which of the following procedures for handling complaints is the decision binding and cannot
be appealed?
(A) Code of procedure
(B) Mediation
(C) Arbitration
(D) Both (B) and (C)
16. Which of the following types of transactions are subÛect to the 5 percent markup policy?
I. Proceeds transactions
II. Riskless transactions
III. Agency transactions
IV. Principal transactions
(A) I, III, and IV
(B) II and III
(C) I and II
(D) I, II, III, and IV
17. Under FINRA rules, all of the following brokerage firm records must be kept for a minimum of
three years ECEPT
(A) ledgers
(B) trade confirmations
(C) order tickets
(D) U4 forms of former employees
18. Brokerɡdealers, banks, investment advisers, and so on must report a possible money-
laundering transaction to
(A) FINRA
(B) FinCEN
(C) FBI
(D) SEC
290 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
19. Which TWO of the following are the maximum penalties for insider trading violations?
I. 20 years in prison per violation
II. 25 years in prison per violation
III. $5 million per individual per violation
IV. $25 million per individual per violation
(A) I and III
(B) I and IV
(C) II and III
(D) II and IV
20. A violation in which a firm attempts to drive up the price of a stock based on false or misleading
information so that the firm can later sell their shares at a higher price is known as
(A) churning
(B) trading ahead
(C) frontrunning
(D) pump and dump
21. Mr. Slick purchased 400 shares of IP Corporation common stock and sold it at a profit prior to
paying for the purchase. This is a violation known as
(A) freeriding
(B) frontrunning
(C) trading ahead
(D) interpositioning
22. As part of FINRA’s business continuity plan, member firms must provide the emergency
contact information for ɗɗɗɗɗɗɗɗɗɗ principal(s) of the firm to contact in the event of an
emergency.
(A) one
(B) two
(C) three
(D) all
23. Which TWO of the following are TRUE?
I. FDIC covers each individual up to $250,000.
II. FDIC covers each individual up to $500,000, of which no more than $250,000 can be cash.
III. SIPC covers each individual up to $250,000.
IV. SIPC covers each individual up to $500,000, of which no more than $250,000 can be cash.
(A) I and III
(B) I and IV
(C) II and III
(D) II and IV
CHAPTER 6  5ules and 5egulations 1o )ooling $round  291
24.
Under FINRA rules, which of the following records must be kept by a brokerage firm for a mini-
mum of six years?
I. Customer account statements
II. U5 forms
III. Records of all trades executed
IV. Sales literature
(A) I, II, and III
(B) II, III, and IV
(C) I and III
(D) I, II, and IV
25. Which of the following records must be kept for the lifetime of a brokerɡdealer?
(A) Records of closed accounts
(B) General ledgers
(C) Partnership documents
(D) All of the above
292 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
Answers and explanations
1. C. The items required on an order ticket are the rep’s identification number, the customer’s
account number, a description of the security, the number of shares, whether the account is
discretionary, whether the customer is buying or selling, whether it’s a market order or
GTC order, whether the trade is for cash or on margin, whether it’s solicited or unsolicited,
the time of the order, and the execution price. Remember that when an order is placed, it’s
usually for immediate execution, so getting a customer’s signature would be nearly
impossible.
2. B. The SEC is a government agency and is not a self-regulatory organization. SROs include
the MSRB, NYSE, CBOE, and FINRA.
3. B. For accounts like Declan Smith’s, the brokerage firm must send out account statements
at least quarterly (every three months); for mutual funds, every six months.
4. A. The ex-dividend date is the first day that the purchaser of a stock will not receive a
previously declared dividend. The ex-dividend date is one business day before the record
date. As a reminder, Saturday and Sunday are not considered business days. So if the record
date was on Monday, the ex-dividend date would be on the previous Friday.
5. C. All of the choices listed are violations. However, pump and dump is the only violation
listed that is a form of market manipulation. Pump and dump is fake news typically
regarding penny stocks that is designed to drive the price of a particular stock up so
that the firm can sell their stock at a large profit.
6. D. All of the choices listed are subÛect to the FINRA 5 percent markup policy (5 percent
markup policy or 5 percent policy). This means that, under normal circumstances in which
you have an average-sized trade and you don’t have to Ûump through hoops to execute the
transaction, you shouldn’t charge more than 5 percent to execute the trade. Now certainly
if the trade is extremely small, you would be able to charge a higher percentage so your
firm doesn’t lose money. Also, if a trade is extremely large, 5 percent would be considered
excessive.
7. D. Certainly all of the choices listed would be considered indications of money laundering.
8. B. Answers II and III are definitely reasons why a person would be statutorily disqualified.
However, answer I doesn’t fit because the person would be statutorily disqualified if they
had a felony conviction in the last 10 years, not 15.
9. D. If a securities licensed individual leaves a brokerage firm, that person has up to two
years to get registered with another firm or they will have to take their license exams again.
10. D. All of the choices listed are violations. Commingling of funds takes place when a firm
combines a customer’s fully paid securities with margined securities, or when a firm
combines its own securities with a customer’s securities. Interpositioning is when two
securities brokerɡdealers act as agents for the same trade, thus requiring the customer to
pay more than one commission. Signatures of convenience are ones in which a customer’s
signature is forged.
CHAPTER 6  5ules and 5egulations 1o )ooling $round  293
11.
C. Stock, corporate bond, and municipal bond transactions settle in two business days after
the trade date (T+2). U.S. government bond and options transactions settle in one business
day after the trade date. As a reminder, cash trades settle the same business day as the
trade date.
12. A. Under Regulation S-P, all brokerɡdealers, investment companies, and investment
advisers must have written policies to protect customer’s records and private information.
This would include things like Social Security numbers, bank account numbers, and so on.
13. B. Although a commission must be included on a trade confirmation for an agency trade,
a markup or markdown does not need to be included for a principal transaction. Remember,
a principal transaction is one in which the dealer is buying for or selling from its own
inventory. Therefore, the price the customer pays or receives already includes a markup
or markdown.
14. B. The first day the stock trades without the dividend is on the ex-dividend date. The
ex-dividend date is one business day before the record date — in this case, Thursday,
October 7.
15. C. Arbitration decisions are binding and non-appealable. Arbitration is certainly less formal
and less costly than going through the court system. As a matter of fact, many brokerage
firms have customers sign an arbitration clause as part of a new account form stating that
the customer agrees to have disputes handled through arbitration.
16. D. All of the choices listed are subÛect to the 5 percent markup policy. The 5 percent markup
policy is designed to help curb overcharging customers for trades. It Ûust means that for
standard-size trades with no other contributing factors that make the trade more difficult,
customers should not be charged more than 5 percent.
17. A. Ledgers, which are customer account statements, must be kept on file for a minimum of
six years, not three. As a reminder, all records must be easily accessible for two years.
18. B. Under the USA Patriot Act, if financial institutions are concerned about the possibility of
money laundering, they must report the transaction(s) to the U.S. Treasury Financial
Crimes Network (FinCEN).
19. A. The maximum penalties for insider trading are $5 million per individual per violation
($25 million per business) and up to 20 years in prison per violation. Although not part of
this question, the maximum civil sanctions are three times the gain or three times the loss
avoided plus disgorgement of profits.
20. D. Pump and dump is a violation in which a firm promotes a security that they own using
false or misleading information to try to pump up the price of the security. After the price
has been driven up, they dump their stock at a profit.
21. A. Freeriding is a violation that takes place when a customer places an order to purchase
a security and sells it at a profit prior to paying for it. Freeriding is not permitted under
Regulation T, and it may require the brokerage firm to freeze the customer’s account for
90 days.
294 PART 4  Playing Nicely: Serving Your Client’s Needs and Following the Rules
22. B. Because of the possibility of an emergency, all firms are required to have business
continuity plans and provide emergency contact information. In addition, all firms must
provide the emergency contact information for two principals to FINRA.
23. B. The FDIC covers each depositor up to $250,000. The SIPC covers each investor up to
$500,000, of which no more than $250,000 can be cash.
24. C. Blotters, which includes records of all trades executed by the brokerage firm; ledgers,
which include customer account statements; general ledgers; position records; account
records; and information on closed accounts must be kept for a minimum of six years.
U5 forms and sales literature must be kept for a minimum of three years.
25. C. Corporate or partnership documents of the member firm must be kept for the lifetime of
