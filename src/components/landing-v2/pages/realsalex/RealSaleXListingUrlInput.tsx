import { useState } from "react";
import { LISTING_URL_PLACEHOLDER } from "./realsalex-content-data";

/**
 * "Paste a listing URL" field used by both hero slides and the final CTA.
 * The long sample Zillow URL is only a hint: it clears as soon as the field
 * is focused and comes back on blur if nothing was typed, as in the source.
 * Uncontrolled on purpose: the front-end-only demo never reads the value.
 */
const RealSaleXListingUrlInput = ({ id }: { id: string }) => {
  const [placeholder, setPlaceholder] = useState(LISTING_URL_PLACEHOLDER);

  return (
    <input
      type="url"
      id={id}
      placeholder={placeholder}
      aria-label="Property listing URL"
      onFocus={() => setPlaceholder("")}
      onBlur={(e) => {
        if (!e.currentTarget.value) setPlaceholder(LISTING_URL_PLACEHOLDER);
      }}
    />
  );
};

export default RealSaleXListingUrlInput;
