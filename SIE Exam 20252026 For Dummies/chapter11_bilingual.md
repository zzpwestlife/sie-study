# Chapter 11: Options: Understanding the Basics of Puts and Calls
# 第 11 章：期权：了解看跌与看涨期权的基础知识

Welcome to the wonderful world of options. I'm sure you've heard stories about the difficulty of options. Put your mind at ease; I'm here to make your life easier. Maybe I'm a little warped, but options are my favorite part of the SIE exam!
欢迎来到奇妙的期权世界。我确定您听说过关于期权难度的种种说法。放轻松；我在这里就是为了让您的学习变得更简单。也许我有点古怪，但期权确实是我在 SIE 考试中最喜欢的部分！

You don't have to do a lot of calculations related to options on the SIE, but the ones that you do have to do are relatively simple. More of the option questions on this exam are about understanding the terminology and rules. But in this chapter, I make facing any math questions you may encounter as simple as possible for you. At the end of this chapter, you get a chance to test your knowledge of options with a chapter quiz.
在 SIE 考试中，您不需要做大量关于期权的计算，而您必须做的那些计算相对简单。本次考试中更多的期权题目是关于术语和规则的理解。但在本章中，我会让您遇到的任何数学问题都变得尽可能简单。在本章末尾，您有机会通过章节测验来测试您的期权知识。

💡 **TIP**
Many more-complex options strategies exist — **straddles, spreads, combinations**, and so on — but you won't need to calculate any of them on the SIE exam. If you're planning to take the Series 7 exam after this one, however, be prepared.
💡 **提示**
还存在许多更复杂的期权策略——**跨式期权 (straddles)**、**价差期权 (spreads)**、**组合期权 (combinations)** 等——但您在 SIE 考试中不需要计算其中的任何一种。然而，如果您计划在此之后参加 Series 7 考试，请做好准备。

---

## 1. Brushing Up on Option Basics
## 1. 复习期权基础知识

Options are just another investment vehicle that (ideally) more-savvy investors can use. Options may be used for **hedging** to protect a securities position or for **speculation**, when looking to trade or exercise an option at a profit.
期权只是另一种投资工具，（理想情况下）更精明的投资者可以使用。期权可用于**套期保值 (hedging)** 以保护证券头寸，或用于**投机 (speculation)**，即寻求通过交易或行使期权来获利。

An owner of an option has the **right, but not the obligation**, to buy or sell an underlying security (stock, bond, and so on) at a fixed price; as **derivatives**, options draw their value from that underlying security. Investors may either exercise the option (buy or sell the security at the fixed price), trade the option in the market, or let it expire.
期权的持有人拥有在固定价格购买或出售标的证券（股票、债券等）的**权利，而非义务**；作为**衍生品 (derivatives)**，期权的价值源自该标的证券。投资者可以选择行使期权（按固定价格买卖证券）、在市场上交易期权，或者让其过期。

All option strategies, whether simple or sophisticated, when broken down are made up of simple call and/or put options. After going over how to read an option, I explain a basic call option and help you figure out how to work with that before moving on to a put option. Next, I discuss options that are in-, at-, or out-of-the-money and the cost of options. After you've sufficiently mastered the basics, the rest (the more-difficult strategies later in this chapter) becomes easier.
所有的期权策略，无论简单还是复杂，拆解开来都是由简单的看涨和/或看跌期权组成的。在介绍如何解读期权之后，我将解释基本的看涨期权，并帮助您在进入看跌期权之前弄清楚如何操作。接下来，我将讨论实值、平值或虚值期权以及期权的成本。在您充分掌握了基础知识之后，其余部分（本章后面更难的策略）就会变得更容易。

---

## 2. Reading an option
## 2. 解读期权

To answer SIE questions relating to options, you have to be able to read an option. The following example shows you how an option may appear on the real exam:
要回答 SIE 考试中有关期权的问题，您必须能够解读期权。以下示例显示了期权在真实考试中可能出现的样式：

**Buy 1 XYZ Apr 60 call at 5**
**买入 1 张 XYZ 4 月 60 看涨期权，权利金为 5**

Here are the seven elements of the option order ticket and how they apply to the example:
以下是期权委托单的七个要素，以及它们如何应用于示例：

1.  **Whether the investor is buying or selling the option: Buy**
    When an investor buys (or **longs, holds, or owns**) an option, they are in a position of power; that investor controls the option and decides whether and when to exercise the option. If an investor is selling (**shorting or writing**) an option, they are obligated to live up to the terms of the contract and must either purchase or sell the underlying stock if the holder exercises the option.
    **投资者是买入还是卖出该期权：买入**
    当投资者买入（或称**做多、持有或拥有**）期权时，他们处于主动地位；该投资者控制着期权，并决定是否以及何时行使期权。如果投资者卖出（**卖空或写入**）期权，他们有义务履行合同条款，如果持有人行使期权，他们必须购买或出售标的股票。
2.  **The contract size: 1**
    You can assume that one option contract is for **100 shares** of the underlying stock. Although this idea isn't as heavily tested on the SIE exam, an investor may buy or sell multiple options (for example, five) if they're interested in having a position in more shares of stock. If an investor owns five option contracts, they're interested in 500 shares of stock, which you will need to know in more detail when taking other exams such as the Series 7.
    **合同规模：1**
    您可以假设一个期权合同代表 **100 股**标的股票。虽然这一概念在 SIE 考试中考查不多，但如果投资者对持有更多股份感兴趣，他们可以买卖多个期权（例如五个）。如果一名投资者拥有五个期权合同，意味着他们对 500 股股票感兴趣，在参加 Series 7 等其他考试时，您需要更详细地了解这一点。
3.  **The name of the stock: XYZ**
    In this case, XYZ is the underlying stock that the investor has a right to purchase at a fixed price.
    **股票名称：XYZ**
    在这种情况下，XYZ 是投资者有权以固定价格购买的标的股票。
4.  **The expiration month for the options: Apr**
    All options are owned for a fixed period of time. The expiration for new options used to be 9 months from the issue date. Now, investors can also purchase options with weekly and quarterly maturities as well as long-term options (**long-term equity anticipation securities**, known affectionately as **LEAPS**). In the preceding example, the option will expire in April — more specifically, at **4 p.m. EST (3 p.m. CST) on the third Friday in April**. (All options expire on the third Friday of the expiration month.)
    **期权的到期月份：4 月**
    所有的期权都持有固定的一段时间。新期权的有效期曾是发行后 9 个月。现在，投资者还可以购买周度到期、季度到期以及长期期权（**长期股权预期证券**，亲切地称为 **LEAPS**）。在前面的例子中，该期权将在 4 月到期——具体来说，是 **4 月第三个星期五的美国东部时间下午 4 点（中部时间下午 3 点）**。（所有期权都在到期月的第三个星期五到期。）

🧠 **REMEMBER**
EST (Eastern Standard Time) is generally easier to recall than CST (Central Standard Time) and is more often tested.
🧠 **请记住**
东部标准时间 (EST) 通常比中部标准时间 (CST) 更容易记住，也更常被考查。

5.  **The strike (exercise) price of the option: 60**
    When the holder (purchaser or owner) exercises the option, they use the option contract to make the seller of the option buy or sell the underlying stock at the strike price. (See the next step for info on determining whether the seller is obligated to buy or sell.) In this case, if the holder were to exercise the option, the holder of the option would be able to purchase 100 shares of XYZ at **$60 per share**.
    **期权的行权价（履约价）：60**
    当持有人（购买者或所有者）行使期权时，他们利用期权合同要求期权卖方按行权价购买或出售标的股票。（见下一步关于确定卖方是否有义务购买或出售的信息。）在本例中，如果持有人行使期权，期权持有人将能够以**每股 60 美元**的价格购买 100 股 XYZ。
6.  **The type of option: call**
    An investor can buy or sell a **call option** or buy or sell a **put option**. **Calls give holders the right to buy** the underlying security at a set price, whereas **puts give holders the right to sell**. So, in the example scenario, the holder has the right to buy the underlying security at the price stated in the preceding step.
    **期权类型：看涨期权 (call)**
    投资者可以买卖**看涨期权 (call option)** 或买卖**看跌期权 (put option)**。**看涨期权赋予持有人买入标的证券的权利**，而**看跌期权赋予持有人卖出的权利**。因此，在示例场景中，持有人有权按前一步所述的价格购买标的证券。
7.  **The premium: 5**
    Of course, an option investor doesn't get to have the option for nothing. An investor buys the option at the **premium**. In this case, the premium is 5, so a purchaser would have to pay **$500** (5 × 100 shares per option).
    **权利金 (Premium)：5**
    当然，期权投资者不会平白无故得到期权。投资者通过支付**权利金**来购买期权。在本例中，权利金为 5，因此购买者必须支付 **500 美元**（5 × 每张期权对应 100 股）。

---

## 3. Looking at call options: The right to buy
## 3. 审视看涨期权：买入权

A **call option** gives the holder (owner) the right, but not the obligation, to buy 100 shares of a security at a fixed price and the seller the obligation to sell the stock at the fixed price. (If the seller does not own 100 shares of the underlying security, they would have to purchase them in the market to be able to fulfill their obligation.) Owners of call options are **bullish** (picture a bull charging forward) because the investors want the price of the stock to increase. If the price of the stock increases above the strike price, holders can either exercise the option (buy the stock at a good price) or sell the option for a profit. By contrast, sellers of call options are **neutral or bearish** (imagine a bear hibernating for the winter) because they want the price of the stock to either stay the same or decrease.
**看涨期权 (call option)** 赋予持有人（所有者）以固定价格购买 100 股证券的权利（而非义务），并赋予卖方以该固定价格出售股票的义务。（如果卖方不持有 100 股标的证券，他们必须从市场上购买才能履行义务。）看涨期权的所有者是**看多 (bullish)** 的（想象一头向前冲的公牛），因为投资者希望股价上涨。如果股价涨到行权价以上，持有人既可以行使期权（以优惠价购买股票），也可以卖出期权获利。相比之下，看涨期权的卖方是**中性或看空 (bearish)** 的（想象一头冬眠的熊），因为他们希望股价保持不变或下跌。

🧠 **REMEMBER**
Assume that Ms. Smith buys 1 DEF Oct 40 call option. Ms. Smith bought the right to purchase 100 shares of DEF at 40. If the price of DEF increases to more than $40 per share, this option becomes very valuable to Ms. Smith because she can purchase the stock at $40 per share and sell it at the market price or sell the option at a higher price. If DEF never eclipses the 40 strike (exercise) price, the option doesn't work out for poor Ms. Smith, and she doesn't exercise the option. However, it does work out for the seller of the option, because the seller receives a premium for selling the option, and the seller gets to pocket that premium.
🧠 **请记住**
假设 Smith 女士购买了 1 张 DEF 10 月 40 看涨期权。Smith 女士购买了以 40 的价格购买 100 股 DEF 的权利。如果 DEF 的价格涨到每股 40 美元以上，这个期权对 Smith 女士来说就变得非常有价值，因为她可以按每股 40 美元购买股票并按市价卖出，或者以更高的价格卖出期权。如果 DEF 的价格从未超过 40 的行权价，那么可怜的 Smith 女士就没法从中获利，她也不会行使该期权。然而，这对期权卖方来说是有利的，因为卖方通过卖出期权收到了权利金，并且可以将这笔权利金收入囊中。

---

## 4. Checking out put options: The right to sell
## 4. 审视看跌期权：卖出权

You can think of a **put option** as being the opposite of a call option (see the preceding section). The holder of a put option has the **right to sell** 100 shares of a security at a fixed price, and the writer (seller) of a put option has the **obligation to buy** the stock if exercised. Owners of put options are **bearish** because the investors want the price of the stock to decrease (so they can buy the stock at market price and immediately sell it at the higher strike price or sell their option at a higher premium). However, sellers of put options are **bullish** (they want the price of the stock to increase), because that would keep the option from going in-the-money (see the next section) and allow them to keep the premiums they received.
您可以将**看跌期权 (put option)** 视为看涨期权的反面（见前一节）。看跌期权的持有人拥有按固定价格**卖出** 100 股证券的**权利**，而看跌期权的写入者（卖方）在期权被行使时有**义务买入**该股票。看跌期权的所有者是**看空**的，因为投资者希望股价下跌（这样他们就可以按市价买入股票，并立即按更高的行权价卖出，或者以更高的权利金卖出期权）。然而，看跌期权的卖方是**看多**的（他们希望股价上涨），因为这会防止期权进入实值状态（见下一节），从而让他们保留收到的权利金。

🧠 **REMEMBER**
Assume that Mr. Jones buys 1 ABC October 60 put option. Mr. Jones is buying the right to sell 100 shares of ABC at 60. If the price of ABC decreases to less than $60 per share, this option becomes very valuable to Mr. Jones. If you were in Mr. Jones's shoes and ABC were to drop to $50 per share, you could purchase the stock in the market and exercise (use) the option to sell the stock at $60 per share, which would make you (the new Mr. Jones) very happy. If ABC never drops below the 60 strike (exercise) price, the option doesn't work out for Mr. Jones and he doesn't exercise the option. However, it does work out for the seller of the option, because the seller receives a premium for selling the option that she gets to keep.
🧠 **请记住**
假设 Jones 先生购买了 1 张 ABC 10 月 60 看跌期权。Jones 先生购买的是按 60 的价格卖出 100 股 ABC 的权利。如果 ABC 的价格跌至每股 60 美元以下，这个期权对 Jones 先生来说就变得非常有价值。如果您处于 Jones 先生的位置，且 ABC 跌至每股 50 美元，您可以从市场上购买股票，并行使（使用）期权按每股 60 美元卖出股票，这会让您（作为新的 Jones 先生）非常开心。如果 ABC 从未跌破 60 的行权价，那么 Jones 先生就没法从中获利，他也不会行使该期权。然而，这对期权卖方来说是有利的，因为卖方通过卖出期权收到了权利金，并且可以保留这笔钱。

---

## 5. Getting your money back: Options in-, at-, or out-of-the-money
## 5. 拿回您的钱：实值、平值或虚值期权

To determine whether an option is in- or out-of-the-money, you have to figure out whether the investor would be able to get at least some of his premium money back if the option were exercised. You can figure out how much an option is in-the-money or out-of-the-money by finding the difference between the market value and the strike price. Here's how you know where in-the-money an option is:

*   **When an option is in-the-money**, exercising the option lets investors sell a security for more than its current market value or purchase it for less — a pretty good deal. The **intrinsic value** of an option is the amount that the option is in-the-money; if an option is out-of-the-money or at-the-money, the intrinsic value is zero.
*   **当期权处于实值 (in-the-money) 时**，行使期权可以让投资者以高于当前市价的价格卖出证券，或以低于市价的价格买入——这非常划算。期权的**内在价值 (intrinsic value)** 就是期权处于实值的金额；如果期权处于虚值或平值，内在价值为零。
*   **When an option is out-of-the-money**, exercising the option means investors can't get the best prices; they'd have to buy the security for more than its market value or sell it for less. Obviously, holders of options that are out-of-the-money don't exercise them.
*   **当期权处于虚值 (out-of-the-money) 时**，行使期权意味着投资者无法获得最优价格；他们必须以高于市价的价格买入证券，或以低于市价的价格卖出。显然，持有虚值期权的人不会行使期权。
*   **When the strike price is the same as the market price**, the option is **at-the-money**; this is true whether the option is a call or a put.
*   **当行权价与市场价格相同时**，期权处于**平值 (at-the-money)**；无论是看涨期权还是看跌期权，这一点都成立。

🧠 **REMEMBER**
Call options — the right to buy — go **in-the-money when the price of the stock is above the strike price**. Suppose that an investor buys a DEF 60 call option and that DEF is trading at 62. In this case, the option would be in-the-money by two points (the option's intrinsic value). If that same investor were to buy that DEF 60 call option when DEF was trading at 55, the option would be out-of-the-money by five points (with an intrinsic value of zero).
A put option — the right to sell — goes **in-the-money when the price of the stock drops below the strike price**. For example, a TUV 80 put option is in-the-money when the price of TUV drops below 80. The reverse holds as well: If a put option is in-the-money when the price of the stock is below the strike price, it must be out-of-the-money when the price of the stock is above the strike price.
🧠 **请记住**
看涨期权（买入权）在**股价高于行权价时进入实值**。假设一名投资者买入了 DEF 60 看涨期权，而 DEF 的交易价格为 62。在这种情况下，该期权处于实值 2 点（即该期权的内在价值）。如果同一位投资者在 DEF 交易价格为 55 时买入该 DEF 60 看涨期权，则该期权处于虚值 5 点（内在价值为零）。
看跌期权（卖出权）在**股价跌至行权价以下时进入实值**。例如，当 TUV 的价格跌破 80 时，TUV 80 看跌期权就处于实值。反之亦然：如果看跌期权在股价低于行权价时处于实值，那么在股价高于行权价时，它必然处于虚值。

⚠️ **WARNING**
Don't take the cost of the option (the premium) into consideration when determining whether an option is in-the-money or out-of-the-money. Having an option that's in-the-money is **not the same as making a profit**. (See the next section for info on premiums.)
⚠️ **警告**
在确定期权是实值还是虚值时，不要考虑期权的成本（权利金）。期权处于实值状态**并不等同于获利**。（有关权利金的信息见下一节。）

💡 **TIP**
Use the phrases **"call up"** and **"put down"** to recall when an option goes in-the-money. **Call up** can help you remember that a call option is in-the-money when the market price is **up**, or above the strike price. **Put down** can help you remember that a put option is in-the-money when the market price is **down**, or below the strike price.
💡 **提示**
使用“**看涨向上** (call up)”和“**看跌向下** (put down)”这两个短语来记忆期权何时进入实值状态。“**看涨向上**”可以帮助您记住，当市场价格**向上**（或高于行权价）时，看涨期权处于实值。“**看跌向下**”可以帮助您记住，当市场价格**向下**（或低于行权价）时，看跌期权处于实值。

📝 **EXAMPLE**
Which TWO of the following options are in-the-money if ABC is trading at 62 and DEF is trading at 44?
I. An ABC Oct 60 call option
II. An ABC Oct 70 call option
III. A DEF May 40 put option
IV. A DEF May 50 put option
(A) I and III (B) I and IV (C) II and III (D) II and IV
The correct answer is (B). Start with the strike (exercise) prices. You're calling up or putting down from the strike prices, not from the market prices. Because call options go in-the-money when the market price is above the strike price, Statement I is the only one that works for ABC. An ABC 60 call option would be in-the-money when the price of ABC is above 60. ABC is currently trading at 62, so that 60 call option is in-the-money. For the ABC 70 call option to be in-the-money, ABC would have to be trading higher than 70. Next, use put down for the DEF put options, because put options go in-the-money when the price of the stock goes below the strike price. Therefore, Statement IV makes sense because DEF is trading at 44, and that's below the DEF 50 put strike price but not the 40 put strike price.

📝 **案例**
如果 ABC 的交易价格为 62，DEF 的交易价格为 44，以下哪两项期权处于实值状态？
I. ABC 10 月 60 看涨期权
II. ABC 10 月 70 看涨期权
III. DEF 5 月 40 看跌期权
IV. DEF 5 月 50 看跌期权
(A) I 和 III (B) I 和 IV (C) II 和 III (D) II 和 IV
正确答案是 (B)。从行权（履约）价开始分析。您是相对于行权价进行“向上”或“向下”判断，而不是相对于市价。因为看涨期权在市价高于行权价时进入实值，所以对于 ABC，陈述 I 是唯一成立的。当 ABC 价格高于 60 时，ABC 60 看涨期权处于实值。ABC 目前价格为 62，因此该 60 看涨期权处于实值。若要 ABC 70 看涨期权进入实值，ABC 的交易价格必须高于 70。接下来，对 DEF 看跌期权使用“看跌向下”，因为看跌期权在股价低于行权价时进入实值。因此，陈述 IV 是正确的，因为 DEF 交易价格为 44，低于 DEF 50 看跌期权的行权价，但不低于 40 看跌期权的行权价。

🧠 **REMEMBER**
When someone is **short** an option, it means that they sold the option. This person is on the opposite side of the transaction than the person who is **long** the option. In this case, the seller received a premium for selling the option. So, someone who is short an option is doing so for income and is hoping that the option expires out-of-the-money so that they get to keep the premium.
When people purchase an option, it is said that they are **long** the option. An investor who is long an option has paid the premium for the option so they need the option to go in-the-money (the price of the underlying security to go in the correct direction) enough for them to not only recoup their premium but also make a few bucks.
🧠 **请记住**
当某人**做空 (short)** 期权时，意味着他们卖出了期权。此人处于与**做多 (long)** 期权者相对的交易位置。在这种情况下，卖方通过卖出期权收到了权利金。因此，做空期权的人是为了获得收入，并希望期权在过期时处于虚值，这样他们就能保留权利金。
当人们购买期权时，就说他们是**做多**期权。做多期权的投资者已经支付了权利金，因此他们需要期权进入实值状态（标的证券价格向正确的方向变动），且程度足以让他们不仅收回权利金，还能赚几块钱。

---

## 6. Paying the premium: The cost of an option
## 6. 支付权利金：期权的成本

The premium of an option is the amount that the purchaser pays for the option. The premium may increase or decrease depending on whether an option goes in- or out-of-the-money, gets closer to expiration, and so on. The premium is made up of many different factors, including:

*   Whether the option is in-the-money (是否处于实值状态)
*   The amount of time the investor has to use the option (投资者使用期权的剩余时间)
*   The volatility of the underlying security (标的证券的波动性)
*   Investor sentiment (例如，现在购买 ABC 股票的看涨期权是否是一种流行趋势)

One of the simple options math questions you may run across on the SIE exam requires you to figure out the **time value** of an option premium. Time value has to do with how long you have until an option expires. There's no set standard for time value, such as every month until an option expires costs buyers an extra $100. However, you can assume that if two options have everything in common except for the expiration month, the one with the longer expiration will have a higher premium. Ideally, the following equation can help keep you from getting a pit in your stomach:

**P = I + T**
**权利金 = 内在价值 + 时间价值**

In this formula, **P** is the premium or cost of the option, **I** is the intrinsic value of the option (the amount the option is in-the-money), and **T** is the time value of the option.

Here's how you find the time value for a BIF Oct 50 call option if the premium is 6 and BIF is trading at 52: Call options (the right to buy) go in-the-money when the price of the stock goes above the strike price (call up). Because BIF is trading at 52 and the option is a 50 call option, it's two points in-the-money; therefore, the intrinsic value is two. Because the premium is six and the intrinsic value is two, the premium must include four as a time value:

P = I + T
6 = 2 + T
T = 4

📝 **EXAMPLE**
Use the following chart to answer the next question.
Stock: LMN | Price: 40.50
| Strike Price | July Calls | Oct Calls | July Puts | Oct Puts |
| :--- | :--- | :--- | :--- | :--- |
| 30 | 13 | 14.5 | 0.25 | 0.50 |
| 40 | 2.5 | 4.5 | 1.5 | 2.75 |
| 50 | 0.25 | 0.75 | 10.5 | 12 |
What is the time value of an LMN October 30 call?
(A) 2.5 (B) 4 (C) 6.25 (D) 9.5
The answer you're looking for is (B). I threw you a curveball by giving you a chart similar to what you may see on the SIE exam. In the chart, look for the October calls column and the 30 strike price row. The intersection is a premium of 14.5. Now find the intrinsic value: call options go in-the-money when the price of the stock is above the strike price. This is a 30 call option, and the price of the stock is 40.50, which is 10.5 above the strike price. Plug in the numbers:
P (14.5) = I (10.5) + T
T = 4

📝 **案例**
利用下表回答下一个问题。
股票：LMN | 市价：40.50
| 行权价 | 7 月看涨 | 10 月看涨 | 7 月看跌 | 10 月看跌 |
| :--- | :--- | :--- | :--- | :--- |
| 30 | 13 | 14.5 | 0.25 | 0.50 |
| 40 | 2.5 | 4.5 | 1.5 | 2.75 |
| 50 | 0.25 | 0.75 | 10.5 | 12 |
LMN 10 月 30 看涨期权的时间价值是多少？
(A) 2.5 (B) 4 (C) 6.25 (D) 9.5
您要找的答案是 (B)。我通过给出一张类似于您在 SIE 考试中可能看到的图表给您出了道难题。在图表中，找到 10 月看涨期权这一列和 30 行权价这一行。交叉点对应的权利金是 14.5. 现在计算内在价值：看涨期权在股价高于行权价时进入实值。这是一个 30 看涨期权，且股价为 40.50，比行权价高出 10.5。代入数字：
权利金 (14.5) = 内在价值 (10.5) + 时间价值
时间价值 = 4

---

## 7. Incorporating Standard Option Math
## 7. 融入标准期权数学计算

I'm here to make your life easier. Prep courses use several different types of charts and formulas to figure out things such as gains or losses, break-even points, maximum gain or loss, and so on. I believe that the easiest way is to use the options chart that follows. It's a simple **Money Out, Money In** chart you can use to plug in numbers. What's great about this chart is that you don't even necessarily have to understand what the heck is going on to determine the answers to most options questions. As this chapter progresses, I show you how incredibly useful the options chart can be.

| Money Out (资金转出) | Money In (资金转入) |
| :--- | :--- |
| | |

If it looks basic, it is — and that's the idea. Any time an investor spends money, you place that value in the **Money Out** side of the options chart, and any time an investor receives money, you place the number in the **Money In** side of the chart.

### Buying or selling call options
### 买入或卖出看涨期权

The most basic options calculations involve buying or selling call or put options. Although using the options chart may not be totally necessary for the more basic calculations, working with the chart now can help you get used to the tool so you'll be ready when the SIE exam tests your sanity with more-complex calculations.

As you work with options charts, you may notice a pattern when determining maximum losses and gains. Table 11-1 gives you a quick reference concerning the maximum gain or maximum loss an investor faces when buying or selling call options. Notice that the buyer's loss is equal to the seller's gain (and vice versa).

### TABLE 11-1: Maximum Gains and Losses for Call Options
### 表 11-1：看涨期权的最大收益与亏损

| Buying or Selling (买入或卖出) | Maximum Loss (最大亏损) | Maximum Gain (最大收益) |
| :--- | :--- | :--- |
| **Buying a call (买入看涨期权)** | Premium (权利金) | Unlimited (无限) |
| **Selling a call (卖出看涨期权)** | Unlimited (无限) | Premium (权利金) |

💡 **TIP**
The key phrase to remember when working with call options is **"calls same"**, which means that the premium and the strike price go on the same side of the options chart.
💡 **提示**
处理看涨期权时要记住的关键短语是“**看涨同侧** (calls same)”，这意味着权利金和行权价都放在期权图表的同一侧。

### Buying call options
### 买入看涨期权

The following steps show you how to calculate the maximum loss and gain for holders of call options (which give the holder the right to buy). I also show you how to find the break-even point. Here's the order ticket for the example calculations:

**Buy 1 XYZ Oct 40 call at 5**
**买入 1 张 XYZ 10 月 40 看涨期权，权利金为 5**

1.  **Find the maximum loss.**
    The holder of an option doesn't have to exercise it, so the most they can lose is the premium. The premium is five, so this investor purchased the option for $500 (5 × 100 shares per option); therefore, you enter that value in the **Money Out** side of the options chart (think "money out of the investor's pocket"). According to the chart, the maximum loss (the most this investor can lose) is $500.
2.  **Determine the maximum gain.**
    To calculate the maximum gain, you have to exercise the option at the strike price. The strike price is 40, so you enter $4,000 (40 strike price × 100 shares per option) under its premium; exercising the call means buying the stock, so that's **Money Out**. When exercising call options, always put the multiplied strike price under its premium. (Remember **calls same**: The premium and the strike price go on the same side of the options chart.)

| Money Out (资金转出) | Money In (资金转入) |
| :--- | :--- |
| $500 (premium) | |
| $4,000 (strike) | |

Because you've already determined the maximum loss, look at the **Money In** portion of the options chart. The Money In is empty, so the maximum gain (the most money the investor can make) is **unlimited**.

When you see a question about the **break-even point**, the SIE examiners are asking, "At what point does this investor not have a gain or loss?" The simplest way to figure out this point for a call option is to use **call up** (remember that call options go in-the-money when the price of the stock goes above the strike price — see the earlier section "Getting your money back"). When using call up, you **add** the strike price to the premium:

**strike price + premium = 40 + 5 = 45**
**行权价 + 权利金 = 40 + 5 = 45**

For this investor, the break-even point is 45. This number makes sense because the investor paid $5 for the option, so the option has to go $5 in-the-money for the investor to recoup the amount they paid. Note: The break-even point is always the same for the buyer and the seller.

### Selling call options
### 卖出看涨期权

Here, I show you how to find the maximum gain and loss, as well as the break-even point, for sellers of call options. Here's the order ticket for the example calculations:

**Sell 1 ZYX Oct 60 call at 2**
**卖出 1 张 ZYX 10 月 60 看涨期权，权利金为 2**

1.  **Determine the maximum gain.**
    The seller makes money only if the holder fails to exercise the option or exercises it when the option is in-the-money by less than the premium received. This investor sold the option for $200 (2 × 100 shares per option); therefore, you enter that amount in the **Money In** side of the options chart. According to the chart, the maximum gain (the most that this investor can make) is the **$200 premium received**. Note: The exercised strike price of $6,000 (60 × 100 shares) doesn't come into play when determining the maximum gain in this example because the holder of the option would exercise the option only if it were in-the-money.
2.  **Find the maximum loss.**
    To calculate the maximum loss, you need to exercise the option at the strike price. The strike price is 60, so you enter $6,000 (60 strike price × 100 shares per option) under its premium. The $6,000 goes in the **Money In** side of the options chart because this investor had to sell the stock to the holder at the strike price (60 × 100 shares). When exercising call options, always enter the multiplied strike price under its premium. (Remember **calls same**: The premium and the strike price go on the same side of the options chart.)

| Money Out (资金转出) | Money In (资金转入) |
| :--- | :--- |
| | $200 (premium) |
| | $6,000 (strike) |

You've already determined the maximum gain; now look at the **Money Out** portion of the options chart. The Money Out is empty, so the maximum loss (the most money the investor can lose) is **unlimited**.

When you see a question about the break-even point, the examiners are asking you, "At what point does this investor not have a gain or loss?" The simplest way to figure this out for a call option is to use **call up**. When using call up, you **add** the strike price to the premium:

**strike price + premium = 60 + 2 = 62**
**行权价 + 权利金 = 60 + 2 = 62**

For this investor, the break-even point is 62. This makes sense because the investor received $2 for the option, so the option has to go $2 in-the-money for this investor to lose the amount that she received for selling the option. Call options go in-the-money when the price of the stock goes above the strike price.

### Buying or selling put options
### 买入或卖出看跌期权

Fortunately, when you're calculating the buying or selling of put options (which give the holder the right to sell), you use the options chart in the same way but with a slight change. Instead of using *calls same* as you do with call options, you use **puts switch** — in other words, you place the premium and the strike price on opposite sides of the options chart.

Table 11-2 serves as a quick reference regarding the maximum gain or maximum loss an investor faces when buying or selling put options.

### TABLE 11-2: Maximum Gains and Losses for Put Options
### 表 11-2：看跌期权的最大收益与亏损

| Buying or Selling (买入或卖出) | Maximum Loss (最大亏损) | Maximum Gain (最大收益) |
| :--- | :--- | :--- |
| **Buying a put (买入看跌期权)** | Premium (权利金) | (Strike – premium) × 100 shares (（行权价 – 权利金）× 100 股) |
| **Selling a put (卖出看跌期权)** | (Strike – premium) × 100 shares (（行权价 – 权利金）× 100 股) | Premium (权利金) |

### Buying put options
### 买入看跌期权

This section explains how to find the maximum loss, maximum gain, and the break-even point for buyers (holders) of put options. Here's the ticket order for the calculations:

**Buy 1 TUV Oct 55 put at 6**
**买入 1 张 TUV 10 月 55 看跌期权，权利金为 6**

1.  **Find the maximum loss.**
    Exercising an option is, well, optional for the holder, so buyers of put options can't lose more than the premium. Because this investor purchased the option for $600 (6 × 100 shares per option), you enter that value in the **Money Out** side of the options chart. The maximum loss (the most that this investor can lose) is the **$600 premium paid**.
2.  **Determine the maximum gain.**
    To find the maximum gain, you have to exercise the option at the strike price. The strike price is 55, so you enter $5,500 (55 strike price × 100 shares per option) on the **opposite side** of the options chart. (Remember **puts switch**: The premium and the strike price go on opposite sides of the options chart.) Exercising the option means selling the underlying stock, so that $5,500 is **Money In**.

| Money Out (资金转出) | Money In (资金转入) |
| :--- | :--- |
| $600 (premium) | $5,500 (strike) |

You've already determined the maximum loss; now look at the **Money In** portion of the options chart. Because you find $4,900 more Money In than Money Out ($5,500 – $600), the maximum gain is **$4,900**.

The break-even point is the security price where the investor doesn't have a gain or loss. The simplest way to figure out this point for a put option is to use **put down** (put options go in-the-money when the price of the stock goes below the strike price). When using put down, you **subtract** the premium from the strike price:

**strike price – premium = 55 – 6 = 49**
**行权价 – 权利金 = 55 – 6 = 49**

For this investor, the break-even point is 49. The investor paid $6 for the option, so the option has to go $6 in-the-money in order for this investor to recoup the amount that they paid. As with call options, the break-even point is always the same for the buyer and the seller.

### Selling put options
### 卖出看跌期权

The following steps show you how to calculate the maximum gain and loss for the seller of a put option. I also demonstrate calculations for the break-even point. Here's the ticket order for the example:

**Sell 1 TUV Sep 30 put at 8**
**卖出 1 张 TUV 9 月 30 看跌期权，权利金为 8**

1.  **Determine the maximum gain.**
    The seller makes money only if the holder of the option fails to exercise it. This investor sold the option for $800 (8 × 100 shares per option); you put that number in the **Money In** side of the options chart. The maximum gain (the most this investor can make) is **$800**.
2.  **Find the maximum loss.**
    To calculate the maximum loss, you have to exercise the option at the strike price. The strike price is 30, so you place $3,000 (30 strike price × 100 shares per option) on the **opposite side** of the options chart. (Remember **puts switch**: The premium and strike price go on opposite sides of the options chart.)

| Money Out (资金转出) | Money In (资金转入) |
| :--- | :--- |
| $3,000 (strike) | $800 (premium) |

You've already determined the maximum gain; now look at the **Money Out** portion of the options chart and compare it to the Money In. The maximum potential loss for this investor is the **$2,200 difference** between the Money Out and the Money In.

You calculate the break-even point for buying or selling puts the same way: You use **put down** (the strike price minus the premium) to figure out the break-even point:

**strike price – premium = 30 – 8 = 22**
**行权价 – 权利金 = 30 – 8 = 22**

For this investor, the break-even point is 22. Because this investor received $8 for the option, the option has to go $8 in-the-money for this investor to lose the amount they received for selling the option. Put options go in-the-money when the price of the stock goes below the strike price (**put down**).

---

## 8. Trading options: Opening and closing transactions
## 8. 交易期权：开仓和平仓交易

### Putting things back where you found them: Doing opposite transactions
### 物归原处：进行相反交易

When distinguishing between opening and closing transactions, your key is to know whether this transaction is the first time or the second time the investor is buying or selling an option: The first time is an **opening**, and the second time is a **closing**. Regardless of whether it is an opening or closing transaction, it must be placed on the order ticket.

Here are your opening transactions:

*   **Opening purchase:** An opening purchase occurs when an investor first buys a call or a put. (开仓买入：投资者第一次买入看涨或看跌期权时发生。)
*   **Opening sale:** An opening sale is when an investor first sells a call or a put. (开仓卖出：投资者第一次卖出（写入）看涨或看跌期权时发生。)

If an investor already has an option position, the investor has to close that position by doing the opposite — through a **closing transaction**. If the investor originally purchased the option, they have to sell to close it. By contrast, if they originally sold the option, they have to purchase to close. Here are the two types of closing transactions:

*   **Closing purchase:** A closing purchase occurs when an investor buys themselves out of a previous option position that they sold. For example, if an investor sold an XYZ Oct 40 call (opening sale), they would have to buy an XYZ Oct 40 call to close out the position. The second transaction is a closing purchase.
*   **Closing sale:** A closing sale occurs when an investor sells themselves out of a previous option position that they purchased. For example, if an investor bought an ABC Sep 60 put (opening purchase), they would have to sell an ABC Sep 60 put to close out the position. The second transaction is a closing sale.

🧠 **REMEMBER**
When determining opening or closing transactions, whether the transactions are both calls or both puts doesn't matter.

📝 **EXAMPLE**
Mr. Kollen previously bought 1 XYZ Oct 65 call at 8 when the market price of XYZ was 64. XYZ is currently trading at 69, and Kollen decides that now would be a good time to sell the option that they previously purchased. The second option order ticket would be marked:
(A) opening sale (B) opening purchase (C) closing sale (D) closing purchase
The right answer is (C). This is the second time that Mr. Kollen does something with the option that he owns; therefore, the move has to be a closing transaction, and you can immediately eliminate (A) and (B). Mr. Kollen has to sell himself out of the position because he owns the option. The second order ticket would have to be marked **closing sale**.

---

## 9. Tricks of the options trade: Calculating gains and losses
## 9. 期权交易技巧：计算损益

In addition to knowing how to mark the order ticket, you have to be able to figure out an investor's gain or loss when trading options. This task isn't difficult after you master the options chart. The key thing to remember is that when an investor closes, they do the **opposite** of what they did before.

📝 **EXAMPLE**
Mrs. Wegner purchased 100 shares of DPY stock at $50 per share. Two weeks later, Mrs. Wegner sold 1 DPY Oct 55 call at 6. Mrs. Wegner held that position for three months before selling the DPY stock at $52 per share and closing the DPY Oct 55 call at 4. What is Mrs. Wegner's gain or loss on the transactions?
(A) $400 gain (B) $400 loss (C) $600 gain (D) No gain or loss
The correct answer is (A). Approach the transactions one at a time:
1. Mrs. Wegner purchased 100 shares at $50: $5,000 in **Money Out**.
2. She sold the DPY 55 call at 6: $600 in **Money In**.
3. Three months later, she sold the stock at $52: $5,200 in **Money In**.
4. To close the option she sold (at 6), she made a closing purchase at 4: $400 in **Money Out**.
Total Money In: $600 + $5,200 = $5,800
Total Money Out: $5,000 + $400 = $5,400
Gain: $5,800 – $5,400 = **$400 gain**.

---

## 10. Got it covered: Stock/option contracts
## 10. 备兑头寸：股票与期权的结合

When an investor purchases or sells option contracts on securities they actually own, that investor is choosing an excellent way to protect (**hedge**) against loss or to bring additional funds into their account, which would only be a partial hedge. The most common form is when an investor sells **covered call options**.

If an investor is selling a call option against a security that they own, the investor is considered to be **covered**. They're covered because if the option is exercised, they have the stock to deliver.

Take the following position as an example:
**Buy 100 shares of QRS at $47 per share**
**Sell 1 QRS Dec 55 call at 4**

1.  **Find this investor's maximum potential loss.**
    The investor purchased 100 shares of QRS at $47 for a total of $4,700 (**Money Out**). Next, they sold 1 QRS Dec 55 call for $400 (**Money In**). This investor has more Money Out than Money In, so the maximum potential loss is **$4,300** ($4,700 minus $400).
2.  **Determine the investor's maximum potential gain.**
    To find the maximum gain, you need to exercise the option at the strike price (55). Take the $5,500 (55 × 100 shares) and place it under its premium (**Money In**). (Remember **calls same**: The exercised strike price and the premium go on the same side of the chart.) Total the two sides and you find that the Money In ($5,900) is $1,200 more than the Money Out ($4,700), so that's the investor's maximum potential gain.

| Money Out (资金转出) | Money In (资金转入) |
| :--- | :--- |
| $4,700 (stock purchase) | $400 (premium) |
| | $5,500 (strike) |
| **$4,700 Total** | **$5,900 Total** |

When the investor is covered, finding the break-even point is nice and easy for stock and options. First, look at how much the investor paid for the stock; then look at how much they paid or received for the option. Find the difference, and you have your break-even point:

**$47 stock price – $4 option premium = $43 break-even point**
**$47 股价 – $4 权利金 = $43 盈亏平衡点**

Because this investor paid $47 per share for the stock and received back $4 per share for selling the option, this investor would need to receive another $43 per share to break even.

🧠 **REMEMBER**
Here's how to find the break-even point for stock and options:
*   If the investor **purchased twice** (bought the stock and bought a protective put option), **add** the stock price and the premium.
*   If the investor **sold twice** (sold short the stock and sold an option), **add** the stock price and the premium.
*   If the investor had **one buy and one sell** (for example, bought the stock and sold the option or sold short the stock and bought the option), **subtract** the premium from the stock price.

---

## 11. Index options
## 11. 指数期权

Besides buying or selling options on an individual stock, you can also buy or sell **index options**. Index options allow investors to speculate on (or hedge against) the price movement of market or segments of the market. Like indexes themselves, index options can be **broad-based** or **narrow-based**. The main broad-based index options are the S&P 500 Index Options (SPX), the S&P 500 Volatility Market Index (**VIX**), and the S&P 100 Index Options (OEX). Narrow-based index options include options on the energy sector (IXE), financial sector (IXM), health care sector (IXV), technology sector (IXU), and so on.

Note: The Chicago Board Options Exchange (CBOE) **VIX** is a measure of how volatile investors believe that the S&P 500 index will be over the next 30 days. Typically, the higher the expectation of volatility, the higher the VIX premiums.

### Premiums of index options
### 指数期权的权利金

Like standard stock options, the pricing unit for index options is 100. This means that, like standard stock options, you **multiply the premium by 100** to get the actual cost.

### Exercises in cash
### 现金结算

Unlike regular stock options in which, when the option is exercised, the underlying security must be delivered, index options are **settled in cash**. This makes sense because it would be very difficult for investors to buy and deliver all the securities covered by an index. If the holder of an index call option exercises their option, they will receive the in-the-money amount multiplied by 100 based on the **closing price at the end of the trading day**, not the current value at the time of exercise.

### Trading hours, settlement, and expiration dates
### 交易时间、结算与到期日

Narrow-based index options trade until 4:00 p.m. Eastern Time, and broad-based index options trade until 4:15 p.m. Eastern Time. Like equity options, the settlement date for index options is the **next business day (T+1)**.

🧠 **REMEMBER**
Index options are either broad-based or narrow-based. So, people may buy or sell index options based on how they believe the market will perform overall (broad-based) or just how a segment of the market will perform (narrow-based). In this case, the same strategy of buying calls and selling puts if you're bullish and buying puts and selling calls if you're bearish still applies. However, investors can also use index options to **hedge (protect) a portfolio** against a market decline.

💡 **TIP**
You'll find that buyers and sellers of index options can incorporate most of the same strategies as equity option buyers and sellers. These strategies include covered writing, hedging, protective puts, straddles and combinations, and uncovered call or put writing.

---

## 12. Gaining Additional Option Insight
## 12. 获取更多期权见解

To help you get a deeper understanding of options, you need to know a few additional things that you will most certainly see on the real-deal SIE exam. Some of these items include who issues the options, what an ROP is, what a risk disclosure document is, and so on.

### Clearing through the OCC
### 通过 OCC 进行结算

The **Options Clearing Corporation (OCC)** is the issuer and guarantor of all listed options. The OCC decides which options will trade as well as their strike prices. In addition, when an investor decides to exercise their option, it's the OCC that **randomly** decides which firm on the other end will be responsible for fulfilling the terms of the option.

🧠 **REMEMBER**
The OCC **does not determine the premium** for options; the premium is determined by investors based on supply and demand, the option's intrinsic value, and the amount of time until the option expires.

### That's ODD: Options risk disclosure document
### 奇怪的 ODD：期权风险披露文件

Because options have a risk that is greater than almost any other investment, all investors must receive an **options risk disclosure document (Options Disclosure Document or ODD)** and a copy of amendments (if any) **prior to their first options transaction** (at the time of or before the account is approved). This ODD explains to investors option terminology and strategies as well as the potential rewards and risks involved in investing in options, such as the chance of losing all money invested or, if selling call options, facing an unlimited maximum loss potential. In addition to the risks, the ODD must also explain tax rules related to options, transaction costs, margin requirements, a special statement for uncovered option writers, and so on.

### Getting the go-ahead: Registered options principal
### 获得许可：注册期权主管 (ROP)

Because of the extra risk of investing in options, all new accounts and option order tickets must be approved and signed by a **registered options principal (ROP)** — a manager with a **Series 4** license, in other words. The registered options principal determines the amount of risk that each investor can take. Certainly, sophisticated investors with a lot of money are able to handle more risk than new option investors with a limited supply of funds.

### Options account agreement
### 期权账户协议 (OAA)

**Within 15 days** after approval of the account by an ROP, the customer must sign and return an **options account agreement (OAA)**. Basically, the OAA just states that the customer has read the ODD, understands the risk associated with trading options, and will abide by the rules and regulations regarding options trading. Should anything change, the customer agrees to notify the firm. If the OAA is not received within 15 days after approval of the account, the customer **cannot open any new options positions**.

### Order ticket
### 委托单

A few things are required on an order ticket that are unique to options. Besides the option that is being bought or sold, you have to write down whether the customer is establishing a **long position** (if they're buying) or a **short position** (if they're selling). In addition, for option sellers, you need to put down whether the seller is **covered** or **uncovered (naked)**.

### Last trade, last exercise, and expiration of an option
### 期权的最后交易、最后行使与到期

Unlike stock certificates, options do expire after a certain period of time. In addition, investors are limited as to when they can trade and exercise an option. Here's the timeline to keep in mind:

*   **Last trade:** The last time an investor can trade an option is **4:00 p.m. Eastern Time on the business day of expiration**. (最后交易：投资者最后一次可以交易期权的时间是**到期营业日的美国东部时间下午 4:00**。)
*   **Last exercise:** The last time an investor can exercise an option is **5:30 p.m. Eastern Time on the business day of expiration**. If an option is in-the-money by at least 1 point at expiration, it will be **automatically exercised**. (最后行使：投资者最后一次可以行使期权的时间是**到期营业日的美国东部时间下午 5:30**。如果在到期时，期权处于实值至少 1 点，它将被**自动行使**。)
*   A vast majority of options (all equity and ETF options) can be exercised any time up 'til expiration — this is known as **American style**. However, there are also **European-style** options that can be exercised **only on the expiration date**. European-style options include capped index options and some foreign currency options. Even though a European-style option can be exercised only at expiration, it can still be traded at any time. (绝大多数期权（所有股票和 ETF 期权）可以在到期前的任何时间行使——这被称为**美式期权**。然而，也存在只能在**到期日当天**行使的**欧式期权**。欧式期权包括封顶指数期权和某些外汇期权。尽管欧式期权只能在到期时行使，但它仍可以在任何时间进行交易。)
*   **Option expiration:** Options expire at **11:59 p.m. Eastern Time on the third Friday of the expiration month**. (期权到期：期权在**到期月第三个星期五的美国东部时间晚上 11:59** 到期。)

---

## 13. Exercise and assignment
## 13. 行使与指派

When taking the SIE exam, you are expected to have a basic understanding of how options are exercised and assigned. Options are cleared through the OCC. Here's how an option is exercised:

When a client wants to exercise an option they own, they contact their broker-dealer. The broker-dealer contacts the OCC. The trade settles in **one business day (T+1)** after the OCC is notified because when the investor is exercising an option, they are actually **trading stock**. (Note: As of May 2024, the settlement cycle for equity options exercises and stock trades has been shortened to T+1).
当客户想要行使他们拥有的期权时，他们会联系其经纪自营商。经纪自营商联系 OCC。在通知 OCC 后的**一个营业日 (T+1)** 内完成交易结算，因为当投资者行使期权时，他们实际上是在**交易股票**。（注：自 2024 年 5 月起，股票期权行权及股票交易的结算周期已缩短至 T+1）。

The steps involved look like this:

1.  Client #1 tells their broker-dealer (Broker A) to exercise the option. (客户 #1 告诉其经纪自营商（经纪商 A）行使期权。)
2.  Broker A notifies the Options Clearing Corporation. (经纪商 A 通知期权结算公司 (OCC)。)
3.  The Options Clearing Corporation chooses the **contra broker** (the broker-dealer on the other side of the transaction — Broker B) **randomly**. (期权结算公司**随机**选择**交易对手经纪商**（交易另一方的经纪自营商——经纪商 B）。)
4.  Broker B **assigns** (chooses the client — Client #2) either **randomly, first-in-first-out (FIFO), or by any other method that is fair and reasonable**. (经纪商 B 通过**随机、先进先出 (FIFO) 或任何其他公平合理的方法****指派**（选择客户——客户 #2）。)
    *   However, Broker B cannot choose the assignment based on size (the one with the most options, the one with the least options, and so on). (然而，经纪商 B 不能根据规模选择指派（即不能选择拥有期权最多或最少的客户等）。)
5.  Client #2 sends the proceeds (stock or cash) to Broker B. (客户 #2 将收益（股票或现金）发送给经纪商 B。)
6.  Broker B sends the proceeds directly to Broker A (the OCC doesn't handle stock or cash). (经纪商 B 将收益直接发送给经纪商 A（OCC 不处理股票或现金）。)

🧠 **REMEMBER**
Although most exercises of options are settled by the delivery of the underlying security, there are some that are settled by the delivery of cash. Specifically, **index options** and **foreign currency options** are always **settled in cash**. This just makes sense because investors can't be expected to deliver an entire index for index options nor be expected to deliver the underlying foreign currency for foreign currency options.

---

## 14. Additional definitions
## 14. 额外定义

For some reason, the SIE exam writers decided you need to know some additional option-specific definitions. I will try to make this as painless as possible.

*   **Aggregate exercise price:** The exercise (strike) price of an option multiplied by the number of units (usually 100 shares) of the underlying security covered by the option contract. (累计行权价：期权的行权（履约）价乘以期权合同所涵盖的标的证券单位数（通常为 100 股）。)
*   **Class of options:** All option contracts of the **same type** (puts or calls) covering the **same underlying security** or index. (期权类别：覆盖**同一标的证券**或指数的所有**同类型**（看跌或看涨）期权合同。)
*   **Series of options:** All option contracts that are of the **same class**, same **expiration date**, and same **exercise price**. (期权系列：属于**同类别**、具有相同**到期日**和相同**行权价**的所有期权合同。)
*   **Clearing member:** A FINRA member that has been admitted to membership in the OCC (Options Clearing Corporation). (结算会员：已获准加入 OCC（期权结算公司）的 FINRA 会员。)
*   **Delta neutral:** An equity options position that has been **fully hedged**. For example, owning 100 shares of ABC stock and owning an at-the-money put on ABC stock. Basically, offsetting long and short positions. (德尔塔中性：已实现**完全对冲**的股票期权头寸。例如，持有 100 股 ABC 股票并持有一份 ABC 股票的平值看跌期权。基本上就是相互抵销多头和空头头寸。)
*   **Outstanding:** An option contract that has been neither closed (closing sale) nor exercised and has not reached the expiration date. (未平仓期权：既未平仓（平仓卖出）也未行使，且尚未达到到期日的期权合同。)

---

## 15. Testing Your Knowledge
## 15. 知识测试

Practice questions (Original English Only)

1. Which of the following are bearish options strategies?
   I. Buying calls II. Buying puts III. Selling calls IV. Selling puts
   (A) I and II (B) I and III (C) II and III (D) II and IV

2. A customer owns call options on ABC common stock. ABC announces a cash dividend. What happens on the ex-dividend date?
   (A) The strike price is reduced to reflect the dividend.
   (B) The strike price remains the same.
   (C) The strike price is increased to reflect the dividend.
   (D) The strike price remains the same unless the customer instructs the OCC to change the strike price.

3. What are possible outcomes for the writer of a covered call option?
   (A) Unlimited profit and unlimited loss
   (B) Unlimited profit and limited loss
   (C) Limited profit and unlimited loss
   (D) Limited profit and limited loss

4. Declan is opening a new options account at a broker-dealer. Declan must return the signed options account agreement
   (A) before the account is approved
   (B) within 15 days after approval of the account
   (C) any time before the first transaction
   (D) sometime before receiving the risk disclosure document

5. An investor is long 1 GHI Oct 30 call. If GHI has a current market value of 33, which of the following is TRUE?
   (A) The option is out-of-the-money.
   (B) The option is at-the-money.
   (C) The option is in-the-money.
   (D) The call has a negative intrinsic value.

6. An investor reads in the newspaper that JKL Dec 60 puts are trading for 6 when JKL is at 64. What is the time value of these options?
   (A) 0 (B) 2 (C) 4 (D) 6

7. Which of the following is TRUE regarding option contracts?
   I. The OCC sets the contract size. II. The OCC sets the strike prices. III. The OCC sets the premiums. IV. The OCC sets the expiration dates.
   (A) I and III (B) I, II, and IV (C) II and III (D) I, II, III, and IV

8. Melissa previously wrote 10 MKR Aug 45 puts for 6 each when the market price of MKR was 46. MKR is currently trading at 41 and the options are one week away from expiration. Melissa would like to buy her way out of that position. If she does, how would the second option order ticket be marked?
   (A) Opening sale (B) Opening purchase (C) Closing sale (D) Closing purchase

9. Who is the issuer and guarantor of all listed options?
   (A) OAA (B) OCC (C) ODD (D) FINRA

10. When is the last time an investor can exercise an option contract?
    (A) 4 p.m. EST on the third Friday of the expiration month
    (B) 5:30 p.m. EST on the third Friday of the expiration month
    (C) 11:59 p.m. EST on the third Friday of the expiration month
    (D) 11:59 p.m. CST on the third Friday of the expiration month

11. What is the break-even point for an investor who writes a Sep 40 call for 3?
    (A) 37 (B) 40 (C) 43 (D) 34

12. What is the maximum potential loss for an investor who shorted 1 XYZ Oct 40 put for 6?
    (A) 3,400 (B) 4,000 (C) 4,600 (D) Unlimited

13. What is the break-even point for an investor who is long 1 ABC Jan 60 put, which was purchased for 4?
    (A) 56 (B) 60 (C) 64 (D) 66

14. Which TWO of the following options are in-the-money if TUV is trading at 43?
    I. TUV 40 calls II. TUV 40 puts III. TUV 50 calls IV. TUV 50 puts
    (A) I and III (B) I and IV (C) II and III (D) II and IV

15. Before opening an options account, a customer must receive an
    (A) OAA (B) OCC (C) ODD (D) All of the above

16. Which TWO of the following options are TRUE of an investor who writes a call option?
    I. The maximum potential gain is the premium. II. The maximum potential loss is the premium. III. The break-even point is the premium added to the strike price. IV. The break-even point is the premium subtracted from the strike price.
    (A) I and III (B) I and IV (C) II and III (D) II and IV

17. If an S&P 500 index call option is in-the-money at expiration, settlement is made by delivery of
    (A) cash (B) a percentage of all of the S&P 500 index stocks (C) an ETF that tracks the S&P 500 (D) longer-term S&P 500 index call options

18. An investor buys 1 TUV Oct 45 put for a premium of $4 and simultaneously buys 100 shares of TUV stock for $45 per share. At expiration, the stock would have to be selling at what price per share for the investor to be able to break even?
    (A) $4 (B) $41 (C) $45 (D) $49

### Answers and explanations

1.  **C.** Put buyers and call sellers are bearish.
2.  **A.** Strike prices are adjusted downwards for cash dividends on the ex-dividend date.
3.  **D.** A covered call writer has limited gain (strike - cost + premium) and limited loss (stock cost - premium).
4.  **B.** The OAA must be signed and returned within 15 days of account approval.
5.  **C.** A 30 call is in-the-money when the stock is at 33 (3 points ITM).
6.  **D.** Premium (6) = Intrinsic (0, since stock 64 > put strike 60) + Time Value (6).
7.  **B.** The OCC sets contract size, strike prices, and expiration dates. Premiums are set by the market.
8.  **D.** To exit a short position, Melissa makes a closing purchase.
9.  **B.** The Options Clearing Corporation (OCC).
10. **B.** 5:30 p.m. ET on the third Friday of the expiration month.
11. **C.** Call break-even = Strike (40) + Premium (3) = 43.
12. **A.** Short put max loss = (Strike - Premium) * 100 = (40 - 6) * 100 = $3,400.
13. **A.** Put break-even = Strike (60) - Premium (4) = 56.
14. **B.** At 43, the 40 calls are ITM (43 > 40) and the 50 puts are ITM (43 < 50).
15. **C.** Customers must receive the ODD at or before account approval.
16. **A.** A call writer's max gain is the premium and break-even is strike + premium.
17. **A.** Index options settle in cash.
18. **D.** Buy stock (45) + Buy put (4) = $49 cost basis. The investor breaks even at $49.
