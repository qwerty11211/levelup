# Levelup

Inspiration
Do you ever struggle to stay motivated to achieve your goals? Do you need some extra incentive to push yourself towards success? If so, then we have an exciting new app that will help you achieve your goals and earn some extra cash while doing it.

What it does
Introducing levelup, an app that lets you join challenges by investing a certain amount of money. You set a goal for yourself and work towards achieving it within the challenge period. If you successfully complete your goal, you'll receive your initial investment back plus a portion of the common pool money, which is filled by those who did not reach their goal. But if you fail to complete the task, the money is reduced from your wallet and goes to the common pool.

Detailed working
First, you choose a challenge to join by investing a specific amount of money. You set a goal for yourself and work towards achieving it within the challenge period. If you successfully complete your goal, you'll receive your initial investment back plus a portion of the common pool money. But if you fail to complete your goal, your invested money will be reduced, and the money goes to the common pool.

At the end of the challenge, the common pool money is randomly awarded to one lucky winner who completed their goal. It's a win-win situation! You'll either achieve your goal and earn some extra cash or motivate yourself to try harder next time.

This app not only incentivizes you to achieve your goals but also creates a supportive community of individuals who are striving towards the same objectives. You can connect with others, share your progress, and motivate each other to achieve your goals together.

How we built it
Django, Verbwire, chatgpt, bootstrap, js

How verbwire is used
Whenever a new challenger/battle is created the app creates a new token
Whenever a user checks in for the daily challenge progress update, it mints the image added by the user as proof for completing the challenge
All the minted NFT's can be viewed in the /nft route
Once a challenge is completed, 1 person is randomly selected as the winner and the fund is withdrawn from the smart contract to the user
Users can also exchange NFTS
How would blockchain help this project
Blockchain technology can be used to enhance the security, transparency, and accountability of the LevelUp app

Blockchain provides an added layer of security to the LevelUp app. It can enable secure and tamper-proof transactions by creating a distributed ledger that records all transactions made within the app. The decentralized nature of blockchain ensures that no single entity can alter or manipulate the records, making it a secure platform for users to join challenges and make transactions.

Blockchain can enhance transparency and accountability in the LevelUp app. It can enable users to track and verify the integrity of transactions made within the app. Blockchain provides an immutable record of all transactions, which can be easily verified by anyone, making it a transparent platform for users to participate in challenges.
