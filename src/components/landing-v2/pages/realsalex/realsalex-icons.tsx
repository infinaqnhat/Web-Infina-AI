import type { CSSProperties, ReactNode } from "react";

/**
 * Stroke icons used across /realsalex. Every icon in realsalex-v2.html shares
 * the same SVG shell (24x24 viewBox, no fill, round caps/joins); only the
 * paths, the rendered size and the stroke width vary, so the shell lives in
 * one component and each call site passes the size/weight the source uses.
 */
const ICON_PATHS = {
  arrowRight: <path d="M5 12h14M13 6l6 6-6 6" />,
  arrowDown: <path d="M12 5v14M6 13l6 6 6-6" />,
  chevronRight: <path d="M9 6l6 6-6 6" />,
  chevronDown: <path d="M6 9l6 6 6-6" />,
  check: <path d="M20 6L9 17l-5-5" />,
  chat: (
    <path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z" />
  ),
  doc: (
    <>
      <path d="M6 2h9l5 5v15H6z" />
      <path d="M14 2v5h5" />
    </>
  ),
  calendar: (
    <>
      <rect x="3" y="4" width="18" height="18" rx="2" />
      <path d="M16 2v4M8 2v4M3 10h18" />
    </>
  ),
  search: (
    <>
      <circle cx="11" cy="11" r="7" />
      <path d="M21 21l-4.35-4.35" />
    </>
  ),
  house: (
    <>
      <path d="M3 11l9-8 9 8" />
      <path d="M5 10v10h14V10" />
    </>
  ),
  bank: (
    <>
      <path d="M3 10l9-6 9 6" />
      <path d="M5 10v10M19 10v10M9 10v10M15 10v10" />
      <path d="M3 21h18" />
    </>
  ),
  people: (
    <>
      <circle cx="9" cy="8" r="3" />
      <path d="M2 20c0-3.3 3.1-5 7-5s7 1.7 7 5" />
      <circle cx="17" cy="9" r="2.3" />
      <path d="M15.5 20c.3-1.8 1.7-3.1 3.5-3.5" />
    </>
  ),
  bars: (
    <>
      <rect x="4" y="12" width="4" height="8" />
      <rect x="10" y="7" width="4" height="13" />
      <rect x="16" y="3" width="4" height="17" />
    </>
  ),
  mail: (
    <>
      <rect x="3" y="5" width="18" height="14" rx="2" />
      <path d="M3 7l9 6 9-6" />
    </>
  ),
  phone: (
    <path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6 19.8 19.8 0 01-3.1-8.7A2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .3 2 .6 2.9a2 2 0 01-.5 2.1L8 10a16 16 0 006 6l1.3-1.2a2 2 0 012.1-.5c.9.3 1.9.5 2.9.6a2 2 0 011.7 2.1z" />
  ),
  pin: (
    <>
      <path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0118 0z" />
      <circle cx="12" cy="10" r="3" />
    </>
  ),
  person: (
    <>
      <circle cx="12" cy="8" r="4" />
      <path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7" />
    </>
  ),
  checkCircle: (
    <>
      <path d="M9 12l2 2 4-4" />
      <circle cx="12" cy="12" r="10" />
    </>
  ),
  answerCheck: (
    <>
      <circle cx="12" cy="12" r="10" />
      <path d="M8 12l3 3 5-6" />
    </>
  ),
  tag: (
    <>
      <path d="M20.6 12.3L12.7 20.2a1 1 0 01-1.4 0l-8-8A1 1 0 013 11.5V4a1 1 0 011-1h7.5a1 1 0 01.7.3l8 8a1 1 0 010 1.4z" />
      <circle cx="7.5" cy="7.5" r="1.2" />
    </>
  ),
  bed: (
    <>
      <path d="M3 18v-6a2 2 0 012-2h14a2 2 0 012 2v6" />
      <path d="M3 18h18M5 10V7a1 1 0 011-1h5a1 1 0 011 1v3" />
    </>
  ),
  alert: (
    <>
      <circle cx="12" cy="12" r="10" />
      <path d="M12 8v5M12 16h.01" />
    </>
  ),
  info: (
    <>
      <circle cx="12" cy="12" r="10" />
      <path d="M12 16v-4M12 8h.01" />
    </>
  ),
  lock: (
    <>
      <rect x="4" y="10" width="16" height="10" rx="2" />
      <path d="M8 10V7a4 4 0 018 0v3" />
    </>
  ),
  bolt: <path d="M13 2L4 14h6l-1 8 9-12h-6l1-8z" />,
  clock: (
    <>
      <circle cx="12" cy="12" r="10" />
      <path d="M12 6v6l4 2" />
    </>
  ),
  external: (
    <>
      <path d="M14 3h7v7M21 3L10 14" />
      <path d="M5 5h6v2H7v10h10v-4h2v6H5z" />
    </>
  ),
} satisfies Record<string, ReactNode>;

export type RealSaleXIconName = keyof typeof ICON_PATHS;

interface RealSaleXIconProps {
  name: RealSaleXIconName;
  size?: number;
  strokeWidth?: number;
  className?: string;
  style?: CSSProperties;
}

export const RealSaleXIcon = ({ name, size = 16, strokeWidth = 2, className, style }: RealSaleXIconProps) => (
  <svg
    viewBox="0 0 24 24"
    width={size}
    height={size}
    fill="none"
    stroke="currentColor"
    strokeWidth={strokeWidth}
    strokeLinecap="round"
    strokeLinejoin="round"
    className={className}
    style={style}
    aria-hidden="true"
  >
    {ICON_PATHS[name]}
  </svg>
);
