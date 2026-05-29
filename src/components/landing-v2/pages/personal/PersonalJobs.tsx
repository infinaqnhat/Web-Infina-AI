// NEW component — mirrors personal.html L1319-1526 <section class="jobs" id="jobs" style="display:none">

/**
 * PersonalJobs
 * Hidden "Top AI Specialist Agents" section — 6 job cards (4 active + 2 coming-soon).
 * Preserved verbatim from personal.html L1319–1526.
 * All inline styles, class names, and image src paths match source exactly.
 * goNow() onclick → window.open("https://infina.ai", "_blank")
 */
const PersonalJobs = () => {
  const goNow = () => {
    window.open("https://infina.ai", "_blank", "noopener,noreferrer");
  };

  return (
    <section className="jobs" id="jobs">
      <div className="container">
        <div className="jobs-head">
          <h2>Top AI Specialist Agents</h2>
        </div>

        <div className="jobs-grid">

          {/* Job 1: Stock Analysis */}
          <article className="job-card" onClick={goNow}>
            <div className="job-visual">
              <span className="job-tag">Only for brokers</span>
              <div style={{ width: "100%", maxWidth: "300px", display: "flex", flexDirection: "column", gap: "16px" }}>
                {/* Stock logos grid */}
                <div style={{ background: "#fff", borderRadius: "16px", padding: "24px", boxShadow: "0 4px 16px rgba(0,0,0,0.06)", border: "1px solid #f0f0f0" }}>
                  <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: "16px" }}>
                    <div className="stock-item" style={{ animationDelay: "0.1s" }}>
                      <div style={{ width: "36px", height: "36px", borderRadius: "8px", background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 8px", boxShadow: "0 4px 12px rgba(0,128,96,0.25)", border: "1px solid #f0f0f0" }}>
                        <img src="/landing-html/uploads/vcb-logo.png" alt="VCB" style={{ width: "28px", height: "28px", objectFit: "contain" }} />
                      </div>
                      <div style={{ fontSize: "11px", color: "#10b981", fontWeight: 600, textAlign: "center" }}>+12.5%</div>
                    </div>
                    <div className="stock-item" style={{ animationDelay: "0.2s" }}>
                      <div style={{ width: "36px", height: "36px", borderRadius: "8px", background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 8px", boxShadow: "0 4px 12px rgba(227,6,19,0.25)", border: "1px solid #f0f0f0" }}>
                        <img src="/landing-html/uploads/mbb-logo.png" alt="MBB" style={{ width: "28px", height: "28px", objectFit: "contain" }} />
                      </div>
                      <div style={{ fontSize: "11px", color: "#10b981", fontWeight: 600, textAlign: "center" }}>+8.3%</div>
                    </div>
                    <div className="stock-item" style={{ animationDelay: "0.3s" }}>
                      <div style={{ width: "36px", height: "36px", borderRadius: "8px", background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 8px", boxShadow: "0 4px 12px rgba(0,107,107,0.25)", border: "1px solid #f0f0f0" }}>
                        <img src="/landing-html/uploads/bidv-logo.png" alt="BID" style={{ width: "28px", height: "28px", objectFit: "contain" }} />
                      </div>
                      <div style={{ fontSize: "11px", color: "#10b981", fontWeight: 600, textAlign: "center" }}>+15.7%</div>
                    </div>
                    <div className="stock-item" style={{ animationDelay: "0.4s" }}>
                      <div style={{ width: "36px", height: "36px", borderRadius: "8px", background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 8px", boxShadow: "0 4px 12px rgba(227,6,19,0.25)", border: "1px solid #f0f0f0" }}>
                        <img src="/landing-html/uploads/vic-logo.png" alt="VIC" style={{ width: "28px", height: "28px", objectFit: "contain" }} />
                      </div>
                      <div style={{ fontSize: "11px", color: "#10b981", fontWeight: 600, textAlign: "center" }}>+9.2%</div>
                    </div>
                    <div className="stock-item" style={{ animationDelay: "0.5s" }}>
                      <div style={{ width: "36px", height: "36px", borderRadius: "8px", background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 8px", boxShadow: "0 4px 12px rgba(0,91,170,0.25)", border: "1px solid #f0f0f0" }}>
                        <img src="/landing-html/uploads/hpg-logo.png" alt="HPG" style={{ width: "28px", height: "28px", objectFit: "contain" }} />
                      </div>
                      <div style={{ fontSize: "11px", color: "#10b981", fontWeight: 600, textAlign: "center" }}>+11.4%</div>
                    </div>
                    <div className="stock-item" style={{ animationDelay: "0.6s" }}>
                      <div style={{ width: "36px", height: "36px", borderRadius: "8px", background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 8px", boxShadow: "0 4px 12px rgba(253,185,19,0.25)", border: "1px solid #f0f0f0" }}>
                        <img src="/landing-html/uploads/mwg-logo.png" alt="MWG" style={{ width: "28px", height: "28px", objectFit: "contain" }} />
                      </div>
                      <div style={{ fontSize: "11px", color: "#10b981", fontWeight: 600, textAlign: "center" }}>+14.1%</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="job-body">
              <h3 className="job-title">Stock Analyst</h3>
              <p className="job-desc">Is ACB stock at 23k VND a good buy right now?</p>
            </div>
            <div className="job-footer">
              <span className="job-stats">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                </svg>
                45.2K
              </span>
              <button className="job-chat-btn">Chat</button>
            </div>
          </article>

          {/* Job 2: Goal-based Investing */}
          <article className="job-card" onClick={goNow}>
            <div className="job-visual">
              <span className="job-tag">Investment Advisor</span>
              <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", padding: "20px" }}>
                <div style={{ width: "100%", maxWidth: "300px", height: "180px", borderRadius: "12px", overflow: "hidden", boxShadow: "0 4px 16px rgba(0,0,0,0.08)" }}>
                  <img src="/landing-html/uploads/house-interior-clean.jpg" alt="Modern House Interior" style={{ width: "100%", height: "100%", objectFit: "cover" }} />
                </div>
              </div>
            </div>
            <div className="job-body">
              <h3 className="job-title">Investment Advisor</h3>
              <p className="job-desc">I have 1B VND, want to buy a 3B house in 2 years - how should I invest?</p>
            </div>
            <div className="job-footer">
              <span className="job-stats">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                </svg>
                32.8K
              </span>
              <button className="job-chat-btn">Chat</button>
            </div>
          </article>

          {/* Job 3: Budget Planning */}
          <article className="job-card" onClick={goNow}>
            <div className="job-visual">
              <span className="job-tag">Budget Planner</span>
              <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", padding: "20px" }}>
                <div style={{ width: "100%", maxWidth: "300px", height: "180px", borderRadius: "12px", overflow: "hidden", boxShadow: "0 4px 16px rgba(0,0,0,0.08)" }}>
                  <img src="/landing-html/uploads/grocery-shopping.png" alt="Grocery Shopping" style={{ width: "100%", height: "100%", objectFit: "cover" }} />
                </div>
              </div>
            </div>
            <div className="job-body">
              <h3 className="job-title">Budget Planner</h3>
              <p className="job-desc">Income 20M VND/month, how much should I spend on rent to save enough?</p>
            </div>
            <div className="job-footer">
              <span className="job-stats">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                </svg>
                24.5K
              </span>
              <button className="job-chat-btn">Chat</button>
            </div>
          </article>

          {/* Job 4: Market News */}
          <article className="job-card" onClick={goNow}>
            <div className="job-visual">
              <span className="job-tag">Market Analyst</span>
              <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", padding: "20px" }}>
                <div style={{ width: "100%", maxWidth: "300px", height: "180px", borderRadius: "12px", overflow: "hidden", boxShadow: "0 4px 16px rgba(0,0,0,0.08)" }}>
                  <img src="/landing-html/uploads/petrolimex.png" alt="Petrolimex Gas Station" style={{ width: "100%", height: "100%", objectFit: "cover" }} />
                </div>
              </div>
            </div>
            <div className="job-body">
              <h3 className="job-title">Market Analyst</h3>
              <p className="job-desc">Any important news affecting Vietnam market today?</p>
            </div>
            <div className="job-footer">
              <span className="job-stats">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                </svg>
                19.3K
              </span>
              <button className="job-chat-btn">Chat</button>
            </div>
          </article>

          {/* Job 5: Insurance Review (Coming Soon) */}
          <article className="job-card" style={{ opacity: 0.7, cursor: "default" }}>
            <div className="job-visual" style={{ background: "linear-gradient(135deg,#dbeafe 0%,#eff6ff 100%)" }}>
              <span className="job-tag" style={{ background: "#3b82f6", color: "#fff" }}>✨ Coming Soon</span>
              <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", padding: "20px" }}>
                <div style={{ background: "#fff", borderRadius: "12px", padding: "20px", boxShadow: "0 4px 12px rgba(0,0,0,0.04)", border: "1px solid #f0f0f0", width: "100%", maxWidth: "280px" }}>
                  <div style={{ display: "grid", gridTemplateColumns: "repeat(2,1fr)", gap: "16px" }}>
                    <div className="insurance-logo" style={{ animationDelay: "0.1s" }}>
                      <div style={{ background: "#f8fafc", borderRadius: "8px", padding: "12px", display: "flex", alignItems: "center", justifyContent: "center", height: "60px", border: "1px solid #e2e8f0" }}>
                        <img src="/landing-html/uploads/pvi-insurance.png" alt="PVI" style={{ maxWidth: "100%", maxHeight: "100%", objectFit: "contain" }} />
                      </div>
                    </div>
                    <div className="insurance-logo" style={{ animationDelay: "0.2s" }}>
                      <div style={{ background: "#f8fafc", borderRadius: "8px", padding: "12px", display: "flex", alignItems: "center", justifyContent: "center", height: "60px", border: "1px solid #e2e8f0" }}>
                        <img src="/landing-html/uploads/prudential.png" alt="Prudential" style={{ maxWidth: "100%", maxHeight: "100%", objectFit: "contain" }} />
                      </div>
                    </div>
                    <div className="insurance-logo" style={{ animationDelay: "0.3s" }}>
                      <div style={{ background: "#f8fafc", borderRadius: "8px", padding: "12px", display: "flex", alignItems: "center", justifyContent: "center", height: "60px", border: "1px solid #e2e8f0" }}>
                        <img src="/landing-html/uploads/baoviet.png" alt="Bao Viet" style={{ maxWidth: "100%", maxHeight: "100%", objectFit: "contain" }} />
                      </div>
                    </div>
                    <div className="insurance-logo" style={{ animationDelay: "0.4s" }}>
                      <div style={{ background: "#f8fafc", borderRadius: "8px", padding: "12px", display: "flex", alignItems: "center", justifyContent: "center", height: "60px", border: "1px solid #e2e8f0" }}>
                        <img src="/landing-html/uploads/aia.png" alt="AIA" style={{ maxWidth: "100%", maxHeight: "100%", objectFit: "contain" }} />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="job-body">
              <h3 className="job-title">Compare Insurance Plans</h3>
              <p className="job-desc">What should I do immediately after a car accident? Which insurance covers what?</p>
            </div>
            <div className="job-footer">
              <span className="job-stats">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                </svg>
                --
              </span>
              <button className="job-chat-btn" style={{ opacity: 0.5, cursor: "not-allowed" }} disabled>Soon</button>
            </div>
          </article>

          {/* Job 6: Travel Planning (Coming Soon) */}
          <article className="job-card" style={{ opacity: 0.7, cursor: "default" }}>
            <div className="job-visual" style={{ background: "linear-gradient(135deg,#dbeafe 0%,#eff6ff 100%)" }}>
              <span className="job-tag" style={{ background: "#3b82f6", color: "#fff" }}>✨ Coming Soon</span>
              <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", padding: "20px" }}>
                <div style={{ width: "100%", maxWidth: "300px", height: "180px", borderRadius: "12px", overflow: "hidden", boxShadow: "0 4px 16px rgba(0,0,0,0.08)" }}>
                  <img src="/landing-html/uploads/luxury-resort.png" alt="Luxury Resort" style={{ width: "100%", height: "100%", objectFit: "cover" }} />
                </div>
              </div>
            </div>
            <div className="job-body">
              <h3 className="job-title">Travel Planner</h3>
              <p className="job-desc">Japan trip in 7 days, budget $3000. Create itinerary + cost breakdown?</p>
            </div>
            <div className="job-footer">
              <span className="job-stats">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                </svg>
                --
              </span>
              <button className="job-chat-btn" style={{ opacity: 0.5, cursor: "not-allowed" }} disabled>Soon</button>
            </div>
          </article>

        </div>
      </div>
    </section>
  );
};

export default PersonalJobs;
