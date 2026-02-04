import json

missing_file = 'pipeline/missing_translations.json'
output_file = 'pipeline/translations_map.json'

translations = {
    "• Transactions by insiders": "• 内部人士交易",
    "• Customer accounts": "• 客户账户",
    "• Trading activities": "• 交易活动",
    "• The issuer’s name, address, and description of its business": "• 发行人的名称、地址及其业务描述",
    "• The company’s articles of incorporation (unless previously supplied)": "• 公司章程（除非之前已提供）",
    "• The names and addresses of the underwriter(s) and all commissions or discounts they will receive from the sale, either directly or indirectly": "• 承销商的名称和地址，以及他们将从销售中直接或间接获得的所有佣金或折扣",
    "• The price at which the security will be offered to the public": "• 证券向公众发售的价格",
    "• The names and addresses of all the company´s control personnel, such as officers, directors,": "• 公司所有控制人员（如高级管理人员、董事）的姓名和地址",
    "• The estimated net proceeds of the sale from the security to be issued and what the proceeds will be used for, including property (initially), or other businesses to be purchased (if any)": "• 拟发行证券销售的预计净收益及其用途，包括购买财产（最初）或其他业务（如有）",
    "• The company’s capitalization (all financing-related debt and equity)": "• 公司资本结构（所有融资相关的债务和股权）",
    "• Complete financial statements, including balance sheets and income statements": "• 完整的财务报表，包括资产负债表和损益表",
    "• Any legal proceedings against the corporation that may affect it": "• 针对公司的任何可能产生影响的法律诉讼",
    "• Any net proceeds derived from any security sold by the issuer in the previous two years, along with the underwriter’s particulars": "• 发行人在过去两年内出售任何证券所得的净收益，以及承销商的详细信息",
    "• The names and addresses of the attorneys who have vouched for the legality of the issue and a copy of their opinion(s) on the legality of the issue": "• 为发行合法性担保的律师姓名和地址，以及他们关于发行合法性的意见书副本",
    "• Any agreements or indentures that might affect the securities being offered": "• 可能影响拟发行证券的任何协议或契约",
    "• Notification (registration by filing): Notification is the simplest form of registration for": "• 通知注册（备案注册）：通知注册是最简单的注册形式，适用于",
    "• Coordination: This method involves registering with the SEC and states at the same time. The": "• 协调注册：此方法涉及同时向SEC和各州注册。",
    "• Qualification: Companies use this registration method for securities that are exempt from": "• 资格注册：公司对以下证券使用此注册方法：豁免于",
    "• Investment banking firm: An investment banking firm is an institution (a broker-dealer) that´s in the business of helping issuers raise money. You can think of investment bankers as being": "• 投资银行公司：投资银行公司是从事帮助发行人筹集资金业务的机构（经纪交易商）。你可以把投资银行家看作是",
    "• Underwriter: An underwriter is a broker-dealer who helps the issuer bring new securities to the public. They take the financial risk and, therefore, receive an extra fee for taking that risk.": "• 承销商：承销商是帮助发行人向公众发行新证券的经纪交易商。他们承担财务风险，因此因承担该风险而获得额外费用。",
    "• Syndicate (syndicate group or syndicate desk): When an issue is too large for one firm": "• 承销团（承销团组或承销台）：当发行规模太大，一家公司无法独自处理时",
    "• Managing (lead) underwriter: The managing underwriter (syndicate manager) is the firm": "• 主承销商（牵头承销商）：主承销商（承销团经理）是指",
    "• Selling group: In the event that the syndicate members need more help selling the securities,": "• 销售组：如果承销团成员需要更多帮助来销售证券，",
    "• All-or-None (AON): If the offering is set up as an AON agreement, all the securities must be": "• 全部或无（AON）：如果发行设置为AON协议，则所有证券必须",
    "• Mini-max: A mini-max offering is one in which a specified minimum number of securities": "• 迷你-最大（Mini-max）：迷你-最大发行是指规定了最低证券数量",
    "• The final offering price": "• 最终发行价格",
    "• The delivery date (when the securities will be available)": "• 交付日期（证券可用的时间）",
    "• Registrar: The registrar is an independent financial institution that works along with a com-": "• 注册处：注册处是一家独立的金融机构，与公司合作",
    "• Transfer agent: The transfer agent is a person or institution that maintains records of a": "• 转让代理人：转让代理人是维护记录的个人或机构",
    "• Securities issued by the U.S. government (Treasury bills, Treasury notes, Treasury bonds, and so on) or federal agencies": "• 美国政府发行的证券（国库券、中期国债、长期国债等）或联邦机构发行的证券",
    "• Municipal securities (local government bonds and notes)": "• 市政证券（地方政府债券和票据）",
    "• Securities issued by banks, savings institutions, and credit unions": "• 银行、储蓄机构和信用合作社发行的证券",
    "• Public utility stocks or bonds": "• 公用事业股票或债券",
    "• Securities issued by religious, educational, or not-for-profit organizations": "• 宗教、教育或非营利组织发行的证券",
    "• Notes, bills of exchange, bankers´ acceptances, and commercial paper (unsecured corporate": "• 票据、汇票、银行承兑汇票和商业票据（无担保公司",
    "• Insurance policies and fixed annuities": "• 保险单和固定年金",
    "• Intrastate offerings (Rule 147): An intrastate offering includes the 80% rule. In order for a company to be eligible for the exemption, at least 80% of the corporation’s assets must be in": "• 州内发行（规则147）：州内发行包括80%规则。为了使公司有资格获得豁免，公司至少80%的资产必须位于",
    "• Regulation A (Reg A, Regulation A+, or Reg A+) offerings: An offering of securities worth": "• 监管A（Reg A，监管A+或Reg A+）发行：价值如下的证券发行",
    "• Regulation D (Reg D) offerings: Also known as a private placement (private securities offering), a Regulation D offering is an offering to no more than 35 unaccredited (nonaccredited)": "• 监管D（Reg D）发行：也称为私募配售（私募证券发行），监管D发行是指向不超过35名非认可（未认可）投资者进行的发行",
    "• Financial institutions (banks, insurance companies, pension funds, and so on)": "• 金融机构（银行、保险公司、养老基金等）",
    "• Insiders of the private placement issuer (officers, directors, and/or owners of 10 percent": "• 私募配售发行人的内部人士（高级管理人员、董事和/或拥有10%",
    "• Investors with a net worth of at least $1 million, excluding primary residence": "• 净资产至少100万美元（不包括主要住所）的投资者",
    "• Investors who have had a net income of at least $200,000 ($300,000 joint) for the": "• 在过去两年中年净收入至少20万美元（共同收入30万美元）的投资者",
    "• Corporations, partnerships, or organizations with a net worth of at least $5 million": "• 净资产至少500万美元的公司、合伙企业或组织",
    "• Reps who are registered and in good standing with the SEC, FINRA, and/or at least one state who have passed the Series 7, Series 65, Series 66, and/or Series 82 exam": "• 在SEC、FINRA和/或至少一个州注册且信誉良好，并通过了Series 7、Series 65、Series 66和/或Series 82考试的代表",
    "• Knowledgeable employees of private funds (hedge funds, private equity funds, and so on)": "• 私募基金（对冲基金、私募股权基金等）的知情员工",
    "• Rural business investment companies (investment companies that raise money to invest in small rural businesses)": "• 农村商业投资公司（筹集资金投资于小型农村企业的投资公司）",
    "• Limited liability companies (LLC) with more than $5 million in assets": "• 资产超过500万美元的有限责任公司（LLC）",
    "• Family offices with at least $5 million in assets under management": "• 管理资产至少500万美元的家族办公室",
    "• Rule 144: This rule covers the sale of restricted stock (such as stock sold through private placement), unregistered, and control securities (stock owned by control persons [affiliates],": "• 规则144：该规则涵盖限制性股票（如通过私募配售出售的股票）、未注册股票和控制证券（控制人[关联方]拥有的股票）的销售",
    "• Rule 144A: This rule allows unregistered domestic and foreign securities to be sold to Qualified": "• 规则144A：该规则允许将未注册的国内和国外证券出售给合格机构买家（QIB）",
    "• 15,000": "• 15,000",
    "• 15,750": "• 15,750",
    "• 16,200": "• 16,200",
    "• 16,250": "• 16,250",
    "• Firm commitment": "• 坚定承诺",
    "• All-or-none": "• 全部或无",
    "• Best efforts": "• 尽力而为",
    "• Mini-max": "• 迷你-最大",
    "• I only": "• 仅I",
    "• II only": "• 仅II",
    "• I, II, and IV": "• I, II和IV",
    "• II, III, and IV": "• II, III和IV",
    "• Which of the following are exempt transactions?": "• 以下哪项属于豁免交易？",
    "• Private placements": "• 私募配售",
    "• Securities issued by the U.S. government": "• 美国政府发行的证券",
    "• Intrastate offerings": "• 州内发行",
    "• Commercial paper": "• 商业票据",
    "• I and III": "• I和III",
    "• II and IV": "• II和IV",
    "• I, II, III, and IV": "• I, II, III和IV",
    "• 41,000": "• 41,000",
    "• 42,000": "• 42,000",
    "• 43,000": "• 43,000",
    "• 44,000": "• 44,000",
    "• 25 days": "• 25天",
    "• 40 days": "• 40天",
    "• 45 days": "• 45天",
    "• 90 days": "• 90天",
    "• An SEC disclaimer": "• SEC免责声明",
    "• The names of the officers of the issuing corporation": "• 发行公司高级管理人员的姓名",
    "• The public offering price": "• 公开发行价格",
    "• An explanation of what the funds raised by the offering would be used for": "• 关于发行筹集资金用途的解释",
    "• I and IV": "• I和IV",
    "• Securities Act of 1933": "• 1933年证券法",
    "• Securities Exchange Act of 1934": "• 1934年证券交易法",
    "• Trust Indenture Act": "• 信托契约法",
    "• All of the above": "• 以上所有",
    "• Which of the following may be included in a tombstone advertisement?": "• 墓碑广告中可能包含以下哪项？",
    "• The number of securities to be sold": "• 待售证券的数量",
    "• The issuer’s name": "• 发行人的名称",
    "• All underwriters’ names": "• 所有承销商的名称",
    "• The post-filing cooling-off period usually lasts about": "• 备案后的冷却期通常持续约",
    "• 20 days": "• 20天",
    "• 30 days": "• 30天",
    "• As soon as the registration statement has been filed": "• 一旦提交了注册声明",
    "• A. In a firm-commitment underwriting, all securities left unsold are retained by the underwriters. All-or-none and mini-max are actually best-efforts underwritings.": "• A. 在坚定承诺承销中，所有未售出的证券均由承销商保留。全部或无和迷你-最大实际上是尽力而为承销。",
    "• D. This one is tricky, because all the transactions are exempt. Regulation D private place- ments and intrastate offerings are exempt based on the type of transactions. But securities issued by the U.S. government and commercial paper are exempt based on the type of security.": "• D. 这个问题很棘手，因为所有交易都是豁免的。监管D私募配售和州内发行是基于交易类型豁免的。但美国政府发行的证券和商业票据是基于证券类型豁免的。",
    "• C. Because the holding period has been met, the maximum number of shares that can be sold by an insider under Rule 144 is 1 percent of the outstanding shares or the average trading volume for the previous four weeks, whichever is greater. Check out the math:": "• C. 由于已满足持有期要求，内部人士根据规则144可以出售的最大股份数量是已发行股份的1%或过去四周的平均交易量，以较大者为准。计算如下：",
    "• D. For IPOs, a final prospectus must be available to all purchasers for 90 days after the effective date.": "• D. 对于IPO，最终招股说明书必须在生效日期后的90天内提供给所有购买者。",
    "• B. All the choices would be in the preliminary prospectus (red herring) except the final offering price. The offering price at this point hasn’t been determined. The offering price, the underwriting spread, and the delivery date would be included in the final prospectus.": "• B. 除了最终发行价格外，所有选项都将包含在初步招股说明书（红鲱鱼）中。此时发行价格尚未确定。发行价格、承销价差和交付日期将包含在最终招股说明书中。",
    "• A. The Securities Act of 1933 (Truth in Securities Act, Paper Act, Full Disclosure Act, Prospectus Act, or New Issues Act) regulates new issues of corporate stocks and bonds. Included in the act are rules to prevent fraud and deception, as well as rules about the issuer’s providing information about itself and the securities being offered.": "• A. 1933年证券法（证券真实法、纸面法、全面披露法、招股说明书法或新发行法）监管公司股票和债券的新发行。该法案包括防止欺诈和欺骗的规则，以及关于发行人提供自身及其所发行证券信息的规则。",
    "• D. Tombstone advertisements may include the name of the issuer, the type of security being offered, the offering price (or approximate offering price), the names of the under- writers, and the number of securities being offered.": "• D. 墓碑广告可能包括发行人的名称、所发行证券的类型、发行价格（或近似发行价格）、承销商的名称以及所发行证券的数量。",
    "• A. The cooling-off period is when an issuer files a registration statement with the": "• A. 冷却期是指发行人向SEC提交注册声明的时间",
    "• B. After the registration is effective (the effective date), the broker–dealer is allowed to": "• B. 注册生效（生效日期）后，经纪交易商被允许",
    "• D. U.S. Treasury securities (Treasury bonds, Treasury notes, Treasury bills, TIPS, and so on), municipal bonds (general obligation bonds, revenue bonds, and so on), and Eurodollar bonds are exempt from SEC registration. U.S. Treasury securities are backed by the federal government, and municipal bonds are backed by a state or local government. Eurodollar bonds are dollar-denominated bonds issued in Europe, and, therefore, must register in the country of issue. ADRs (American Depositary Receipts) are receipts for foreign securities traded in the United States and, therefore, must be registered in the United States.": "• D. 美国国债（长期国债、中期国债、国库券、通胀保值债券等）、市政债券（一般义务债券、收益债券等）和欧洲美元债券免于SEC注册。美国国债由联邦政府支持，市政债券由州或地方政府支持。欧洲美元债券是在欧洲发行的以美元计价的债券，因此必须在发行国注册。ADR（美国存托凭证）是在美国交易的外国证券的收据，因此必须在美国注册。"
}

with open(missing_file, 'r', encoding='utf-8') as f:
    items = json.load(f)

result = []
for item in items:
    block_id = item['id']
    en_text = item['en_text']
    
    # Try exact match first
    zh_text = translations.get(en_text)
    
    if not zh_text:
        print(f"Warning: No translation found for: {en_text}")
        zh_text = "[Translation Pending]"
        
    result.append({
        'id': block_id,
        'translation': zh_text
    })

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
    
print(f"Created {output_file} with {len(result)} items.")
