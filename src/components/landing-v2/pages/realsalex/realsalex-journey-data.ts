import { UPLOADS } from "./realsalex-content-data";
import type { AccentHeading } from "./realsalex-content-data";
import type { RealSaleXIconName } from "./realsalex-icons";

/**
 * The two "How it works" journeys in realsalex-v2.html: one per tab, same
 * 4-card layout. The last step of each is the "done" (green) step.
 * `photoMobile` is set only where the source uses a different crop on the
 * stacked mobile cards.
 */
export interface JourneyStep {
  num: string;
  title: string;
  sub: string;
  icon: RealSaleXIconName;
  pill: string;
  text: string;
  photo: string;
  photoMobile?: string;
  alt: string;
}

export interface JourneySectionCopy extends AccentHeading {
  eyebrow: string;
  sub: string;
  steps: JourneyStep[];
}

/** Timeline under the cards, identical on both tabs. Mobile shows only `stage`. */
export const journeyStages = [
  { label: "Many questions", stage: "Exploration" },
  { label: "Qualified interest", stage: "Intent" },
  { label: "Serious conversation", stage: "Negotiation" },
  { label: "Action", stage: "Transaction" },
];

export const buyingJourney: JourneySectionCopy = {
  eyebrow: "The agent's advantage",
  title: "Know what matters. ",
  accent: "Know where to help.",
  sub: "A focused briefing brings together the buyer's stated needs, timing, open questions, and next step. You can start informed and carry that understanding through the purchase.",
  steps: [
    {
      num: "01",
      title: "Share at first contact.",
      sub: "Before you know their budget or timeline.",
      icon: "chat",
      pill: "First contact",
      text: "Share Home Concierge for 123 Main Street before you know the buyer's needs, budget, or timeline.",
      photo: `${UPLOADS}/buyer-journey-contact.jpg`,
      alt: "A woman smiling at her phone at home, receiving a first message",
    },
    {
      num: "02",
      title: "Build understanding through conversation.",
      sub: "Learn as the buyer replies.",
      icon: "doc",
      pill: "Ongoing conversation",
      text: "Learn from volunteered answers and update the buyer's profile as their plans develop.",
      photo: `${UPLOADS}/buyer-journey-conversation.jpg`,
      alt: "A hand writing on a new home checklist",
    },
    {
      num: "03",
      title: "Step in when your expertise matters.",
      sub: "A concrete reason to connect.",
      icon: "calendar",
      pill: "Your expertise",
      text: "A tour request, a changed move date, or an unresolved concern gives you a concrete reason to connect.",
      photo: `${UPLOADS}/buyer-journey-connect.jpg`,
      photoMobile: `${UPLOADS}/buyer-journey-connect-mobile.jpg`,
      alt: "An agent smiling while calling a buyer",
    },
    {
      num: "04",
      title: "Carry the context through closing.",
      sub: "Keep priorities in view.",
      icon: "check",
      pill: "Through closing",
      text: "Use those priorities to guide the search, clarify concerns, and keep purchase tasks in view.",
      photo: `${UPLOADS}/buyer-journey-closing.jpg`,
      photoMobile: `${UPLOADS}/buyer-journey-closing-mobile.jpg`,
      alt: "A house with a SOLD sign in the front yard",
    },
  ],
};

export const listingJourney: JourneySectionCopy = {
  eyebrow: "The entire buyer journey",
  title: "Keep the conversation moving toward ",
  accent: "a decision.",
  sub: "Property Expert is designed to carry questions forward as interest becomes a showing, an offer, and a transaction. You see where your attention can help.",
  steps: [
    {
      num: "01",
      title: "Discovery",
      sub: "From questions to informed interest.",
      icon: "chat",
      pill: "Answer questions",
      text: "Answer property questions from current listing materials and invite the buyer to explore what matters.",
      photo: `${UPLOADS}/journey-discovery.jpg`,
      alt: "A buyer relaxing at home, reading messages on her phone",
    },
    {
      num: "02",
      title: "Showing",
      sub: "From interest to a showing.",
      icon: "calendar",
      pill: "Prepare a tour",
      text: "Capture a tour request and the buyer's questions so you can prepare a relevant visit.",
      photo: `${UPLOADS}/journey-showing.jpg`,
      alt: "An agent and a buyer talking during a home showing",
    },
    {
      num: "03",
      title: "Offer",
      sub: "From showing to a real conversation.",
      icon: "doc",
      pill: "Route key questions",
      text: "Ask what remains unresolved. Route requests about price, terms, or repairs to the right people.",
      photo: `${UPLOADS}/journey-offer.jpg`,
      alt: "A hand reviewing a printed real estate offer",
    },
    {
      num: "04",
      title: "Closing",
      sub: "From accepted offer to closing.",
      icon: "check",
      pill: "Organize next steps",
      text: "Organize document requests, inspection questions, and agreed milestones.",
      photo: `${UPLOADS}/journey-closing.jpg`,
      alt: "A house with a SOLD sign in the front yard",
    },
  ],
};
