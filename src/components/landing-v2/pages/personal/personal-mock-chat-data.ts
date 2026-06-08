/**
 * personal-mock-chat-data.ts
 * Data for the PersonalJobPicker and PersonalMockChat components.
 * Extracted from the "Mock Chat" and "Job Picker" scripts in personal.html.
 * All conversation texts are verbatim from the source.
 */

export interface ConversationData {
  specialist: string;
  avatar: string;
  response: string;
  followups: string[];
}

export interface JobChip {
  label: string;
  /** true = real conversation chip, false = soon/cta chip */
  active: boolean;
  /** if true, the card opens infina.ai instead of the mock-chat */
  cta?: boolean;
  /** badge text shown on the card */
  badge?: string;
  /** question count display string, e.g. "2.4M" */
  count?: string;
}

/** Hardcoded chip lists per tab, verbatim from jobData in personal.html */
export const JOB_DATA: Record<string, JobChip[]> = {
  finance: [
    { label: 'Should I buy this stock?', active: true, badge: 'Brokers only', count: '2.4M' },
    { label: 'Where should I invest my money?', active: true, count: '1.8M' },
    { label: 'Am I spending too much this month?', active: true, count: '940K' },
    { label: "What's moving the market today?", active: true, count: '1.2M' },
    { label: 'Which insurance plan fits me?', active: true, count: '670K' },
    { label: 'How do I pay less tax?', active: true, count: '1.1M' },
    { label: 'Can I afford this loan?', active: true, count: '580K' },
    { label: 'How long to reach my savings goal?', active: true, count: '430K' },
    { label: 'Have something else on mind? Chat with me.', active: false, cta: true },
  ],
  lifestyle: [
    { label: 'Plan my trip', active: true, count: '320K' },
    { label: 'Plan my weekly meals', active: true, count: '210K' },
    { label: 'Have something else on mind? Chat with me.', active: false, cta: true },
  ],
};

/**
 * All conversations verbatim from personal.html inline JS.
 * Keys match chip labels exactly so lookup is direct.
 */
export const CONVERSATIONS: Record<string, ConversationData> = {
  'Should I buy this stock?': {
    specialist: 'Stock Analyst',
    avatar: '📈',
    response:
      "ACB looks interesting at current levels. Here's my read:\n\n• P/E of 8.2x — below the banking sector average\n• Volume rising for 3 consecutive sessions (bullish signal)\n• Short-term target: 26,000 VND\n\nI'd suggest a partial entry now with a stop-loss at 21,500 VND to protect your downside.",
    followups: ["What's my risk level?", 'Show me similar stocks', 'Set a price alert'],
  },
  'Where should I invest my money?': {
    specialist: 'Investment Advisor',
    avatar: '💼',
    response:
      "With a 2-year horizon, here's a balanced split I'd recommend:\n\n• 50% Government bonds — stable ~6.2% yield, low risk\n• 30% Blue-chip stocks — VCB, MBB for growth exposure\n• 20% Short-term savings deposit — liquid, capital protected\n\nWant me to model this for a specific amount?",
    followups: ['Model for 100M VND', 'Higher risk option?', 'How do I start?'],
  },
  'Am I spending too much this month?': {
    specialist: 'Budget Planner',
    avatar: '📊',
    response:
      "On 20M/month, a healthy breakdown looks like:\n\n• Needs (rent, food, transport): max 10M — 50%\n• Lifestyle & wants: up to 6M — 30%\n• Savings: at least 4M — 20%\n\nIf your essentials already exceed 10M, you're over budget on the basics. Share your top 3 expenses and I'll pinpoint where to cut.",
    followups: ['Break down by category', 'How to cut food costs?', 'Build a monthly budget'],
  },
  "What's moving the market today?": {
    specialist: 'Market Analyst',
    avatar: '🏦',
    response:
      "VN-Index is up 0.8% this morning. Key movers:\n\n• Banking sector leading — MBB +2.1%, VCB +1.3%\n• Foreign investors net-bought 45B VND in the morning session\n\nWatch tonight: US Fed minutes release may spark short-term volatility.",
    followups: ['Which stocks to watch?', 'Real estate sector outlook?', 'Set a market alert'],
  },
  'Which insurance plan fits me?': {
    specialist: 'Insurance Advisor',
    avatar: '🛡️',
    response:
      "For a working adult in their 30s, I'd recommend two layers:\n\n• Term life insurance — 500M coverage at ~2M/month\n• Health insurance — with outpatient coverage included\n\nOne thing to avoid: investment-linked plans. Keep investing and insurance separate — better returns and better coverage.",
    followups: ['Compare top plans', 'What does it cover?', 'Get a quote'],
  },
  'How do I pay less tax?': {
    specialist: 'Tax Advisor',
    avatar: '🧾',
    response:
      "Three legal ways to cut your tax bill:\n\n• Claim all dependents — 4.4M deduction per person/month\n• Voluntary pension fund — deductible up to 1M/month\n• If freelancing — register as a business for a flat 7% rate instead of progressive rates up to 35%\n\nWant me to calculate how much each saves you?",
    followups: ['Calculate my tax bill', 'Tell me about dependents', 'Freelancer tax guide'],
  },
  'Can I afford this loan?': {
    specialist: 'Loan Advisor',
    avatar: '🏠',
    response:
      "Rule of thumb: keep repayments under 30% of monthly income.\n\nOn 20M/month your ceiling is 6M/month.\n\nFor a 500M loan at 9% interest:\n• 10-year term → ~6.3M/month (slightly over your limit)\n• 15-year term → ~5M/month (comfortable)\n\nI'd go with the 15-year term to give yourself breathing room.",
    followups: ['Simulate different terms', 'Compare lenders', "What's my debt ratio?"],
  },
  'How long to reach my savings goal?': {
    specialist: 'Savings Planner',
    avatar: '🎯',
    response:
      "Here's how long it takes to reach 100M:\n\n• Saving 4M/month at 6% return → ~22 months\n• Saving 6M/month at 6% return → ~15 months\n\nThe 6% assumes government bonds — safe and accessible. Got existing savings? I can factor that in for a more accurate timeline.",
    followups: ['Factor in existing savings', 'Show higher-yield options', 'Set a savings reminder'],
  },
  'Plan my trip': {
    specialist: 'Travel Planner',
    avatar: '✈️',
    response:
      "Da Nang + Hoi An, 7 days — here's how 10M breaks down:\n\n• Flights (return): ~2.5M\n• Accommodation: ~3M (mid-range hotels)\n• Food & drinks: ~2M\n• Activities & entrance fees: ~1.5M\n• Local transport: ~1M\n\nTotal: ~10M with a small buffer. Want me to build the day-by-day itinerary?",
    followups: ['Build day-by-day itinerary', 'Try Phu Quoc instead', 'Find cheaper flights'],
  },
  'Plan my weekly meals': {
    specialist: 'Nutrition Advisor',
    avatar: '🥗',
    response:
      "Simple balanced plan on 500K/week:\n\n• Mon / Wed / Fri — Grilled chicken + rice + stir-fry (~30K/meal)\n• Tue / Thu — Tofu + egg + soup (~20K/meal)\n• Weekend — Flex meal or eat out\n\nTip: Batch-cook Sunday evening. Saves 2 hours on weekday mornings and cuts impulse food spending.",
    followups: ['Make it high-protein', "I'm vegetarian", 'Generate a shopping list'],
  },
};
