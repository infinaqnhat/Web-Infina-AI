import { UPLOADS } from "./realsalex-content-data";
import type { AgentTab } from "./realsalex-content-data";

/**
 * Copy for the "What your client gets" demo card in realsalex-v2.html that
 * is not part of the canned Q&A: the build checklist and everything on the
 * card (heading, advisor, gallery, specs, share link) that changes per tab.
 */

/** Checklist shown while "Create Home Concierge" builds the (scripted) advisor. */
export const BUILD_STEPS = [
  "Reading the listing",
  "Pulling county records and tax history",
  "Matching comparable sales within 0.4 miles",
  "Reading the seller's disclosure",
  "Publishing your advisor",
];

/** Everything on the demo card that changes with the tab. */
export interface DemoTabCopy {
  heading: { title: string; accent: string; sub: string };
  advisorName: string;
  brokerage: string;
  agentFirst: string;
  roleLabel: string;
  askTitle: string;
  loadingTitle: string;
  builtTitle: string;
  shareLink: string;
  footer: string;
  gallery: { src: string; alt: string }[];
  address: string;
  specs: string[];
}

/** The main photo is passed by file name: the two listings do not share a naming scheme for it. */
const galleryFor = (slug: string, mainFile: string, place: string, mainAlt: string) => [
  { src: `${UPLOADS}/${mainFile}`, alt: mainAlt },
  { src: `${UPLOADS}/property-${slug}-living.jpg`, alt: `${place} living room` },
  { src: `${UPLOADS}/property-${slug}-kitchen.jpg`, alt: `${place} kitchen` },
  { src: `${UPLOADS}/property-${slug}-bedroom.jpg`, alt: `${place} primary bedroom` },
  { src: `${UPLOADS}/property-${slug}-backyard.jpg`, alt: `${place} backyard patio` },
];

export const demoTabCopy: Record<AgentTab, DemoTabCopy> = {
  buying: {
    heading: {
      title: "What your ",
      accent: "client gets",
      sub: "A private page for this property, with an advisor that answers instantly and cites its sources.",
    },
    advisorName: "Alex Rivera's Home Concierge",
    brokerage: "Meridian Realty · Austin, TX",
    agentFirst: "Alex",
    roleLabel: "Advisor",
    askTitle: "Ask anything about 123 Main Street",
    loadingTitle: "Building your advisor",
    builtTitle: "Alex Rivera's Home Concierge is live for this listing.",
    shareLink: "advisor.realsalex.co/alex/123-main-st",
    footer: "Alex sees every question and can join the conversation at any point.",
    gallery: galleryFor("123-main", "property-123-main.jpg", "123 Main Street", "123 Main Street, Austin TX exterior photo"),
    address: "123 Main Street, Austin TX",
    specs: ["$845,000", "4 bd · 3 ba", "2,410 sq ft", "46 days on market"],
  },
  listing: {
    heading: {
      title: "What ",
      accent: "buyers get",
      sub: "A private page for this listing, with a Property Expert that answers instantly and cites its sources.",
    },
    advisorName: "148 Maple Ave's Property Expert",
    brokerage: "Listed by Sarah Jenkins, Broker",
    agentFirst: "Sarah",
    roleLabel: "Property Expert",
    askTitle: "Ask anything about 148 Maple Ave",
    loadingTitle: "Building your Property Expert",
    builtTitle: "148 Maple Ave's Property Expert is live for this listing.",
    shareLink: "propertyexpert.realsalex.co/148-maple-ave",
    footer: "Sarah sees every question and can join the conversation at any point.",
    gallery: galleryFor(
      "148-maple",
      "property-148-maple-main.jpg",
      "148 Maple Ave",
      "148 Maple Ave, Mapleton exterior photo"
    ),
    address: "148 Maple Ave, Mapleton",
    specs: ["$748,000", "4 bd · 3 ba", "2,410 sq ft", "Just listed"],
  },
};
