# Chapter 14: Securities Markets: Taking Orders and Executing Trades
# 第 14 章：证券市场：接受订单与执行交易

Part of your function as a registered rep will be to understand and explain to customers (and potential customers) how the stock market works. I designed this chapter with that in mind (along with the fact that you need to know this stuff for the SIE, of course).
作为一名登记代表，您的部分职责是理解并向客户（及潜在客户）解释股票市场是如何运作的。我设计本章时正是基于这一考量（当然，这也是因为您需要掌握这些内容以应对 SIE 考试）。

In this chapter, I cover the basics of exchanges and the over-the-counter (OTC) market, along with some of the active participants who help the market run smoothly (at least most of the time). Pay particular attention to the sections “Reviewing basic order types” and “Factoring in order features,” because you’ll definitely use that information every day after you pass the SIE and corequisite tests.
在本章中，我将涵盖交易所和场外交易 (OTC) 市场的基本知识，以及一些帮助市场平稳运行（至少大部分时间是这样）的活跃参与者。请特别关注“回顾基本订单类型”和“考虑订单特征”这两节，因为在您通过 SIE 及相关进阶考试后，您每天都会用到这些信息。

---

## 1. Shopping at Primary and Secondary Markets
## 1. 在一级市场与二级市场购物

Depending on whether the securities are new or outstanding, they trade in either the primary or secondary market.
根据证券是新发行的还是已流通的，它们分别在一级市场或二级市场进行交易。

### Buying new in the primary market
### 在一级市场购买新股

The **primary market** (new issue market) is where the issuer receives the proceeds from the sale of securities. A security that has never been offered or sold to the public is considered a new issue. Here are the three types of offerings on the primary market:
**一级市场 (Primary market)**（新发行市场）是发行人获取证券销售收入的市场。从未向公众提供或出售过的证券被视为新发行证券。以下是一级市场的三种发行类型：

*   **Initial public offering (IPO)**: An IPO is the first time a corporation ever sells stock to the public to raise capital. When a corporation is in the process of issuing securities for the first time, it’s said to be **going public**.
*   **首次公开募股 (IPO)**：IPO 是公司第一次向公众出售股票以筹集资金。当公司第一次发行证券时，就被称为**上市 (going public)**。
*   **Primary offering**: A primary offering is the issuer market, where the issuer is selling shares to raise money. Certainly, an IPO falls into that category. However, the corporation usually holds shares back for future use; it later pulls those securities out of storage and sells them in a **subsequent** (add-on, additional, or follow-up) offering, which is also a primary offering.
*   **一级发行 (Primary offering)**：一级发行是发行人市场，即发行人通过出售股份来筹集资金。IPO 当然属于这一类。然而，公司通常会保留一部分股份供未来使用；之后再将这些证券从“储藏室”中取出，并在**后续**（增发、追加或随后的）发行中出售，这同样属于一级发行。
*   **Combined (split) offering**: This type of offering is a combination of new securities and a large block of outstanding or previously outstanding securities.
*   **组合（混合）发行 (Combined/split offering)**：这种发行类型是新证券与大笔已流通（或之前已流通）证券的结合。

🧠 **REMEMBER**
When securities are sold in the primary market, the **bulk of the sales proceeds goes to the issuer** and the balance goes to the entity or entities responsible for selling the securities to the public — the underwriter(s) and selling group members (if any).
🧠 **请记住**
当证券在一级市场出售时，**销售收益的大部分归发行人所有**，余额则归负责向公众销售证券的实体——即承销商和销售小组成员（如果有的话）。

### Buying used in the secondary market
### 在二级市场购买“二手”股

When the securities are already trading in the market, the sales proceeds go to **another investor** instead of to the issuer. The secondary market, also called the **aftermarket**, consists of the following categories:
当证券已经在市场上交易时，销售收益流向**另一名投资者**，而不是发行人。二级市场（也称为**后续市场 aftermarket**）由以下类别组成：

*   **First market**: Trading of **listed securities** on an exchange floor (e.g., NYSE). (第一市场：在交易所大厅交易的**上市证券**。)
*   **Second market**: Trading of **unlisted securities** over-the-counter (OTC). (第二市场：场外交易的**非上市证券**。)
*   **Third market**: The trading of **exchange-listed securities** in the over-the-counter (OTC) market. (第三市场：在场外交易 (OTC) 市场交易的**交易所上市证券**。)
*   **Fourth market**: The trading of securities **between institutions** without the use of a brokerage firm. These trades are typically executed through **electronic communication networks (ECNs)** such as Instinet. (第四市场：**机构之间**不通过经纪公司而直接进行的证券交易。这些交易通常通过 Instinet 等**电子通信网络 (ECNs)** 执行。)

💡 **TIP**
You’re more likely to get a question on the third or fourth market than the first or second.
💡 **提示**
在考试中，您遇到关于第三或第四市场的问题的可能性比第一或第二市场要大。

---

## 2. Making the Trade
## 2. 执行交易

After securities are issued publicly, they may trade on an exchange or on the OTC market.
证券公开发行后，可以在交易所或场外交易 (OTC) 市场进行交易。

### Auctioning securities at securities exchanges
### 在证券交易所拍卖证券

Exchanges are **auction markets**, where bidders and sellers get together to execute trades.
交易所是**拍卖市场**，买卖双方聚集在一起执行交易。

*   All exchanges have a **trading floor**. (所有交易所都有一个交易大厅。)
*   Each security listed on an exchange has its own **trading post** (location) on the floor. (在交易所上市的每种证券在大厅都有自己的交易点。)
*   **Designated market makers (DMMs)** (formerly specialists): These professionals manage the auction market for a particular security. Their purpose is to maintain a **“fair and orderly market.”** A DMM can act as a broker or a dealer. An important function of a DMM is to keep track of and execute **limit orders**. (**指定做市商 (DMMs)**（原名特种商）：这些专业人士管理特定证券的拍卖市场。他们的目的是维持**“公平且有序的市场”**。DMM 既可以作为经纪人，也可以作为自营商。DMM 的一个重要功能是记录并执行**限价单**。)

### Negotiating trades over the counter
### 在场外协商交易

Unlike exchanges, the OTC market is considered a **negotiated market**. Instead of yelling out prices, traders buy and sell by way of telephone or computer transactions.
与交易所不同，场外交易 (OTC) 市场被视为**协商市场**。交易者不是大声喊价，而是通过电话或计算机交易来买卖证券。

*   **OTCBB (Over the Counter Bulletin Board)**: A quotation service operated by FINRA for unlisted (non-Nasdaq) securities. (OTCBB：由 FINRA 运营的为非上市（非纳斯达克）证券提供的报价服务。)
*   **Pink Market (Pink Sheets)**: For corporations too small to be placed on the OTCBB. They are not required to meet listing requirements or file with the SEC. (**粉单市场**：适用于规模太小而无法在 OTCBB 上市的公司。他们不需要满足上市要求或向 SEC 备案。)

🧠 **REMEMBER**
**U.S. government and municipal bonds trade only OTC.**
🧠 **请记住**
**美国政府债券和市政债券仅在场外交易 (OTC) 交易。**

---

## 3. Understanding the Role of a Broker-Dealer
## 3. 理解经纪自营商的角色

For a firm to be considered a **broker-dealer**, it must buy and sell securities from its own account and act as a middleman for securities not in inventory.
对于一家被称为**经纪自营商 (broker-dealer)** 的公司，它必须既能利用自有账户买卖证券，又能为不在库存中的证券充当中间人。

*   **Broker (Agent)**: A firm is acting as a broker when it **doesn't use its own inventory**. A broker charges a **commission**. The terms *broker* and *agent* may be used interchangeably. (经纪人（代理人）：当公司**不使用自有库存**时，它是在作为经纪人行事。经纪人收取**佣金**。术语“经纪人”和“代理人”可以互换使用。)
*   **Dealer (Principal)**: A firm is acting as a dealer when it **uses its own inventory**. A dealer charges a **markup** (when selling) or a **markdown** (when buying). The terms *dealer*, *principal*, and *market maker* may be used interchangeably. (自营商（主事人）：当公司**使用自有库存**时，它是在作为自营商行事。自营商收取**加价 (markup)**（卖出时）或**减价 (markdown)**（买入时）。术语“自营商”、“主事人”和“做做市商”可以互换使用。)

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

*   **Market order**: For immediate execution at the **best price available**. (市价单：按**当前最优价格**立即执行。)
*   **Selling short**: Selling securities they don't actually own (borrowed from a lender). A short seller is **bearish**. All short sales must be executed in **margin accounts**. (卖空：卖出并不实际拥有的证券（从借出人处借入）。卖空者是**看空**的。所有卖空交易必须在**融资账户**中执行。)
*   **Stop order**: Used for **protection** (limit loss or lock in gains). (止损单：用于**保护**（限制损失或锁定收益）。)
    *   **Buy stop order**: Protects a short position. Triggered if the market price touches a particular price or **higher**. (**买入止损单**：保护空头头寸。如果市场价格达到特定价格或**更高**时触发。)
    *   **Sell stop order**: Protects a long position. Triggered if the market price touches a particular price or **lower**. (**卖出止损单**：保护多头头寸。如果市场价格达到特定价格或**更低**时触发。)
*   **Limit order**: Used when a customer is specific about the price. (限价单：当客户对价格有具体要求时使用。)
    *   **Buy limit**: Buy at the limit price or **lower**. (**买入限价**：按限价或**更低**价格买入。)
    *   **Sell limit**: Sell at the limit price or **higher**. (**卖出限价**：按限价或**更高**价格卖出。)

🧠 **REMEMBER**
Because stop and limit orders are price-specific, they **may or may not be executed**.
🧠 **请记住**
由于止损单和限价单对价格有特定要求，它们**可能成交，也可能不成交**。

---

## 5. Factoring in order features
## 5. 考虑订单特征

*   **Day**: Canceled if not filled by the end of the trading day. (当日有效单：如果交易日结束前未成交则取消。)
*   **Good-'til-canceled (GTC)**: Open until executed or canceled. (撤销前有效单 (GTC)：一直开启，直到执行或被撤销。)
*   **Not held (NH)**: Gives the broker discretion about **timing**. NH orders deal only with timing, not the security or quantity. (不限时订单 (NH)：赋予经纪人在**时机选择**上的自主权。NH 订单仅涉及择时，不涉及证券品种或数量。)
*   **Fill or kill (FOK)**: Execute **entire order immediately** or cancel. (全额成交或取消 (FOK)：**立即全额执行**订单，否则取消。)
*   **Immediate or cancel (IOC)**: Execute as much as possible immediately; cancel the rest. (立即成交或取消 (IOC)：立即执行尽可能多的部分，取消剩余部分。)
*   **All-or-none (AON)**: Execute in entirety or not at all (doesn't have to be immediate). (全额成交 (AON)：要么全额执行，要么不执行（不一定非要立即执行）。)

---

## 6. Recognizing Different Types of Investors
## 6. 识别不同类型的投资者

*   **Retail investors**: Nonprofessionals trading for their own accounts. (散户投资者：为自己的账户进行交易的非专业人士。)
*   **Accredited investors**: Investors with more money or knowledge. Includes financial institutions, insiders, and individuals with an **annual income of $200,000** ($300,000 joint) or a **net worth of $1 million** (excluding primary residence). (合格投资者：拥有更多资金或知识的投资者。包括金融机构、内幕人士，以及**年收入达 20 万美元**（夫妻共有 30 万美元）或**净资产达 100 万美元**（不包括主要住所）的个人。)
*   **Institutional investors**: Entities that invest a lot of money (e.g., banks, mutual funds, pension funds). (机构投资者：投入大量资金的实体（如银行、共同基金、养老基金）。)

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
