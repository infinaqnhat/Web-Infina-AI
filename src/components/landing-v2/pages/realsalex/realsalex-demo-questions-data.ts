import type { AgentTab } from "./realsalex-content-data";

/**
 * Canned Q&A for the "What your client gets" demo card in realsalex-v2.html.
 * FRONT-END ONLY: there is no model behind the card. Chips pick an entry,
 * free text is keyword-matched against these entries (see matchQuestion in
 * RealSaleXDemoChat). `%A` in `close` is replaced by the tab's agent first name.
 */
export interface DemoAnswer {
  q: string;
  lead: string;
  points: { n: string; t: string }[];
  close: string;
  sources: string[];
}

/** Buyer-agent tab: 123 Main Street, Austin TX. */
const buyingQuestions: DemoAnswer[] = [
  {
    q: "What concerns would you have about this house?",
    lead: "Three things I would investigate before making an offer.",
    points: [
      { n: "01", t: "The roof is original to the 2004 build. The disclosure notes a leak repaired above the garage in 2019, but no replacement: plan on $18–24k, and ask for a roof certification inside your inspection period." },
      { n: "02", t: "It sits at the edge of the Shoal Creek 500-year floodplain. No claims on record, but most lenders on this street require a flood policy: roughly $640 a year." },
      { n: "03", t: "Two homes on the same block closed at $329 and $336 a foot in the last 90 days. This one is asking $351, a gap worth a conversation before you write." },
    ],
    close: "I would want %A's read on the roof before you decide, she has walked four homes on this street this year. Want me to flag this for her?",
    sources: ["MLS", "Seller Disclosure", "Public Records", "Agent Notes"],
  },
  {
    q: "Is $845,000 fair for this street?",
    lead: "It is priced above the block, and there is a reason for part of it.",
    points: [
      { n: "01", t: "Median close on Main Street over the last six months is $332 a foot. At $845,000 this is $351, about 6% above the block." },
      { n: "02", t: "The 2022 kitchen and the detached studio are real: comparable renovated homes in Bryker Woods carry a $20–30k premium." },
      { n: "03", t: "It has been listed 46 days with one $20,000 reduction. Sellers at that point have usually accepted that the first number was optimistic." },
    ],
    close: "%A has negotiated three offers in this pocket this year. She is the right person to tell you where the number actually lands.",
    sources: ["MLS", "Public Records", "Comparable Sales", "Agent Notes"],
  },
  {
    q: "What would my monthly payment be?",
    lead: "At list price with 20% down, here is the shape of it.",
    points: [
      { n: "01", t: "$676,000 financed at today's 30-year rates works out to roughly $4,350 a month in principal and interest." },
      { n: "02", t: "Travis County taxes on the current assessment add about $1,190 a month, and insurance, including the flood policy most lenders want here, about $310." },
      { n: "03", t: "All in, expect $5,850 a month. There is no HOA on this street, worth $150–250 a month against comparable new-build options." },
    ],
    close: "These are estimates from public assessment data, not a quote. %A can introduce you to a lender who will put real numbers on it.",
    sources: ["Public Records", "Tax Assessor", "MLS"],
  },
  {
    q: "Why has it been on the market 46 days?",
    lead: "Three plausible reasons, in the order I would weigh them.",
    points: [
      { n: "01", t: "It listed in late July, the slowest four weeks of the Austin year. Homes on this street that listed in April averaged 19 days." },
      { n: "02", t: "The original price was $865,000, about 8% over the block. The reduction to $845,000 came at day 31." },
      { n: "03", t: "There is nothing in the disclosure or permit history that would explain the time on market: no failed inspection, no back-out noted." },
    ],
    close: "Nothing here looks like a hidden problem. If you want, %A can ask the listing agent directly whether an offer has fallen through.",
    sources: ["MLS", "Seller Disclosure", "Permit History"],
  },
  {
    q: "How are the schools, and would we be zoned to them?",
    lead: "You would be zoned to all three, and one of them has a caveat.",
    points: [
      { n: "01", t: "Casis Elementary, O. Henry Middle and Austin High: all three are inside the attendance boundary as drawn for the current year." },
      { n: "02", t: "O. Henry has been over capacity for two years and the district has discussed boundary changes. Nothing is adopted, but worth watching if you have a child entering sixth grade." },
    ],
    close: "I am reading published boundaries, which the district can change. %A tracks these proposals and can tell you where the conversation stands.",
    sources: ["School District", "Public Records", "Agent Notes"],
  },
];

/** Listing-agent tab: 148 Maple Ave, Mapleton. */
const listingQuestions: DemoAnswer[] = [
  {
    q: "What should I know about this property?",
    lead: "Here's a quick snapshot before you dig deeper.",
    points: [
      { n: "01", t: "Built in 2005, HVAC was replaced in 2021 and the roof was reshingled in 2016, no reported leaks since." },
      { n: "02", t: "It's on well and septic rather than city utilities, common in Mapleton, budget for a septic inspection during your due diligence period." },
      { n: "03", t: "Mapleton Elementary is rated 8/10 and a 5-minute walk away." },
    ],
    close: "Want me to pull the full disclosure or the septic service history next?",
    sources: ["MLS", "Seller Disclosure", "Public Records"],
  },
  {
    q: "What do the disclosures say about the roof?",
    lead: "The disclosure covers the roof directly.",
    points: [
      { n: "01", t: "The roof was reshingled in 2016 and the seller reports no leaks or repairs since." },
      { n: "02", t: "A minor granule loss was noted near the chimney flashing during the seller's last walkthrough, cosmetic, not flagged as active." },
      { n: "03", t: "No warranty transfer is mentioned, ask the listing agent if the original roofing warranty is still active." },
    ],
    close: "I can request the roofing invoice from 2016 if you want it in writing.",
    sources: ["Seller Disclosure", "MLS"],
  },
  {
    q: "How does this price compare with recent nearby sales?",
    lead: "Here's how $748,000 stacks up against the neighborhood.",
    points: [
      { n: "01", t: "Two comparable 4-bed homes within half a mile closed in the last 90 days at $305 and $320 a square foot." },
      { n: "02", t: "At $748,000 for 2,410 sq ft, this listing works out to about $310 a square foot, right in the middle of that range." },
      { n: "03", t: "It's just listed, so there's no price-history signal yet, comps suggest the asking price is fair, not aggressive." },
    ],
    close: "Want a full comps sheet with addresses and sale dates?",
    sources: ["MLS", "Comparable Sales", "Public Records"],
  },
  {
    q: "What should I pay attention to during the showing?",
    lead: "A few specific things worth checking in person.",
    points: [
      { n: "01", t: "Test water pressure and check for any musty smell near the crawlspace access, common tell for well/septic homes." },
      { n: "02", t: "Look at the attic insulation depth, the disclosure doesn't specify when it was last upgraded." },
      { n: "03", t: "Ask to see the septic service records and confirm the tank was last pumped." },
    ],
    close: "I can put together a printable showing checklist if that's useful.",
    sources: ["Seller Disclosure", "Agent Notes"],
  },
  {
    q: "Are there any potential concerns I should investigate?",
    lead: "Nothing major, but two items worth a closer look.",
    points: [
      { n: "01", t: "The disclosure notes a small foundation settling crack patched in 2020, the seller reports no movement since in yearly checks." },
      { n: "02", t: "Being on well and septic means water quality and tank condition depend on maintenance history, not municipal oversight." },
      { n: "03", t: "No inspection report is attached yet since this just listed, plan to schedule one early in your offer timeline." },
    ],
    close: "Want me to flag these for a home inspector's checklist before your first showing?",
    sources: ["Seller Disclosure", "Public Records", "Agent Notes"],
  },
];

export const demoQuestions: Record<AgentTab, DemoAnswer[]> = {
  buying: buyingQuestions,
  listing: listingQuestions,
};
