import type { AgentTab } from "./realsalex-content-data";
import type { DemoAnswer } from "./realsalex-demo-questions-data";

/**
 * Buyer-purpose analyses behind the persona pills on the demo card
 * (realsalex-v2.html PERSONAS_BUYER / PERSONAS_LISTING). Each pill swaps the
 * thread to a canned answer framed for that buyer goal. The card opens on
 * the "buyer" (first-time buyer) persona.
 */
export type PersonaKey = "buyer" | "upgrade" | "investment" | "flip" | "vacation";

export const PERSONA_OPTIONS: { key: PersonaKey; label: string }[] = [
  { key: "buyer", label: "First-time buyer" },
  { key: "upgrade", label: "Upgrade" },
  { key: "investment", label: "Investment" },
  { key: "flip", label: "Flip" },
  { key: "vacation", label: "Vacation home" },
];

const buyingPersonas: Record<PersonaKey, DemoAnswer> = {
  buyer: {
    q: "What should I know before making an offer?",
    lead: "Three things worth knowing before you commit.",
    points: [
      { n: "01", t: "At $845,000 with 10% down, expect a monthly payment near $5,850 including taxes and insurance, budget accordingly against your income." },
      { n: "02", t: "The roof is original to the 2004 build with a repaired leak in 2019, ask for a roof certification inside your inspection period." },
      { n: "03", t: "It sits at the edge of the Shoal Creek 500-year floodplain, most lenders here require a flood policy, roughly $640 a year." },
    ],
    close: "I can pull the full disclosure and flood zone map if you want to go deeper before your offer.",
    sources: ["MLS", "Seller Disclosure", "Public Records"],
  },
  upgrade: {
    q: "Is this a good move up from my current home?",
    lead: "Here's how this compares to a typical move-up purchase.",
    points: [
      { n: "01", t: "At 2,410 sq ft with 4 beds and 3 baths, this runs about 25% larger than the median starter home in this pocket of Austin." },
      { n: "02", t: "It has been on the market 46 days with one $20,000 price reduction, a sign there may be room to negotiate on your move-up budget." },
      { n: "03", t: "Factor in about 6% combined agent commission plus transfer taxes on your sale, typically $48k-56k on a similar-priced departure home." },
    ],
    close: "Want me to estimate your net proceeds from selling your current home first?",
    sources: ["MLS", "Local Market Data", "Public Records"],
  },
  investment: {
    q: "Would this work as a rental property?",
    lead: "Here's the rental math on this one.",
    points: [
      { n: "01", t: "Comparable rentals in this pocket of Austin lease for about $3,800/month. Against this list price, gross yield is roughly 5.4%, cap rate after expenses lands near 4.0%." },
      { n: "02", t: "With 25% down at current rates, estimated cash-on-cash return is about 3.6%, below the 8% target most investors look for." },
      { n: "03", t: "At $3,800 rent against an estimated $3,550 monthly debt service, DSCR is approximately 1.07, below the 1.20 most DSCR lenders require." },
    ],
    close: "This looks tight as a straight rental. Want me to model a house-hack scenario, or check nearby comps with stronger yield?",
    sources: ["MLS", "Rental Comps", "Lender Guidelines"],
  },
  flip: {
    q: "What's my max offer if I want to flip this?",
    lead: "Running the 70% rule on this one.",
    points: [
      { n: "01", t: "Two comparable renovated 4-bed homes on this block closed at $329 and $336 a square foot in the last 90 days, putting ARV near $810,000." },
      { n: "02", t: "The kitchen and studio look updated, but the original roof and dated systems suggest a medium rehab, plan on $35-45 per square foot, or roughly $95,000." },
      { n: "03", t: "70% of ARV ($567,000) minus rehab ($95,000) puts your max offer around $472,000, well below the $845,000 asking price." },
    ],
    close: "At the current price, this doesn't pencil as a flip. Want me to flag similar listings closer to that offer range?",
    sources: ["MLS", "Comparable Sales", "Renovation Cost Data"],
  },
  vacation: {
    q: "Could this work as a vacation home with rental income?",
    lead: "Here's what matters for a vacation-use purchase.",
    points: [
      { n: "01", t: "Austin requires a short-term rental license and this property's zoning allows it, but confirm HOA restrictions if one applies to this street." },
      { n: "02", t: "Similar homes in this area average around 52% occupancy annually, concentrated around festival season and university events." },
      { n: "03", t: "Property tax, insurance and a rental-ready policy for this size home typically run $1,050-1,250/month before any mortgage." },
    ],
    close: "Want me to pull the exact permit rules for this zoning district and nearby occupancy data?",
    sources: ["Local Ordinance", "Rental Market Data", "Public Records"],
  },
};

const listingPersonas: Record<PersonaKey, DemoAnswer> = {
  buyer: {
    q: "What should I know before making an offer?",
    lead: "Three things worth knowing before you commit.",
    points: [
      { n: "01", t: "At $748,000 with 10% down, expect a monthly payment near $4,950 including taxes and insurance, budget accordingly against your income." },
      { n: "02", t: "HVAC was replaced in 2021 and there are no reported roof leaks, but ask for a home inspection to confirm attic insulation and water heater age." },
      { n: "03", t: "Mapleton Elementary is rated 8/10 and a 5-minute walk away, a common reason buyers choose this block." },
    ],
    close: "I can pull the full inspection report and school zoning map if you want to go deeper before your offer.",
    sources: ["MLS", "Public Records", "School District Data"],
  },
  upgrade: {
    q: "Is this a good move up from my current home?",
    lead: "Here's how this compares to a typical move-up purchase.",
    points: [
      { n: "01", t: "At 2,410 sq ft with 4 beds and 3 baths, this runs about 30% larger than the median starter home in Mapleton." },
      { n: "02", t: "Homes in this price range are averaging 12 days on market this quarter, plan your sale timeline to avoid carrying two mortgages." },
      { n: "03", t: "Factor in about 6% combined agent commission plus transfer taxes on your sale, typically $45k-55k on a similar-priced departure home." },
    ],
    close: "Want me to estimate your net proceeds from selling your current home first?",
    sources: ["MLS", "Local Market Data", "Public Records"],
  },
  investment: {
    q: "Would this work as a rental property?",
    lead: "Here's the rental math on this one.",
    points: [
      { n: "01", t: "Comparable rentals nearby lease for about $3,400/month. Against this list price, gross yield is roughly 5.5%, cap rate after expenses lands near 4.1%." },
      { n: "02", t: "With 25% down at current rates, estimated cash-on-cash return is about 3.8%, below the 8% target most investors look for." },
      { n: "03", t: "At $3,400 rent against an estimated $3,050 monthly debt service, DSCR is approximately 1.11, below the 1.20 most DSCR lenders require." },
    ],
    close: "This looks tight as a straight rental. Want me to model a house-hack scenario, or check nearby comps with stronger yield?",
    sources: ["MLS", "Rental Comps", "Lender Guidelines"],
  },
  flip: {
    q: "What's my max offer if I want to flip this?",
    lead: "Running the 70% rule on this one.",
    points: [
      { n: "01", t: "Recently renovated 4-bed comps within half a mile closed between $305 and $320 a square foot, putting ARV near $770,000." },
      { n: "02", t: "From the listing photos, this looks like a medium rehab (kitchen, baths, cosmetic), plan on $35-45 per square foot, or roughly $95,000." },
      { n: "03", t: "70% of ARV ($539,000) minus rehab ($95,000) puts your max offer around $444,000, well below the $748,000 asking price." },
    ],
    close: "At the current price, this doesn't pencil as a flip. Want me to flag similar listings closer to that offer range?",
    sources: ["MLS", "Comparable Sales", "Renovation Cost Data"],
  },
  vacation: {
    q: "Could this work as a vacation home with rental income?",
    lead: "Here's what matters for a vacation-use purchase.",
    points: [
      { n: "01", t: "Mapleton requires a short-term rental permit and caps rentals at 120 nights per year in this zoning district, confirm before counting on rental income." },
      { n: "02", t: "Similar homes in the area average 48% occupancy annually, concentrated in summer and holiday weekends, not a year-round income stream." },
      { n: "03", t: "Property tax, insurance and a rental-ready policy for this size home typically run $950-1,100/month before any mortgage." },
    ],
    close: "Want me to pull the exact permit rules for this zoning district and nearby occupancy data?",
    sources: ["Local Ordinance", "Rental Market Data", "Public Records"],
  },
};

export const demoPersonas: Record<AgentTab, Record<PersonaKey, DemoAnswer>> = {
  buying: buyingPersonas,
  listing: listingPersonas,
};
