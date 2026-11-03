Cafe Calle Ocho - Ordering Prototype
Student: Lincoln Guimaraes Valadares
Course: EGN475 - Week 1, Assignment 2
Date: November 3, 2026
Option: A - Cafe Calle Ocho, Little Havana
Repository: https://github.com/lincolnvaladares-7/egn475-cafe-valadares
1. Project choice
I chose Option A, Cafe Calle Ocho, because ordering coffee and food is a familiar process that can be represented with a small, practical prototype. The project also continues the cafe direction of my first Flask exercise while using the business specified in this assignment. It will focus on clear orders and visible kitchen progress.
2. Problem statement
For this proposed scenario, Cafe Calle Ocho currently takes orders verbally at the counter and passes handwritten tickets to the kitchen. This causes unclear item details, missed orders, and uncertainty about preparation progress for customers and kitchen staff. Our prototype will provide a digital menu, order placement, and a kitchen board that moves orders through received, preparing, ready, and picked up so that staff can track requests consistently and customers can understand their order status.

Scenario note: The current workflow is a design assumption for the class prototype, not a verified observation of a real business.
3. Target users and personas
Customer persona: Marta Perez
Role: A regular customer who stops for breakfast before work.
Main goals: Find available items quickly, submit an accurate order, and know when it is ready.
Frustrations today: Waiting in a busy line, repeating an order, and not knowing whether the kitchen has started it.
Comfort with technology: Moderate; comfortable with simple websites on a phone, but prefers a short process without creating an account.
Quote: "I want to order my cafe con leche and know when I can pick it up."
Staff persona: Luis Ramirez
Role: Kitchen team member responsible for preparing and handing off orders.
Main goals: See each order clearly, prepare orders in arrival order, and update progress without losing tickets.
Frustrations today: Difficult handwriting, misplaced tickets, and repeated questions about whether an order is ready.
Comfort with technology: Basic to moderate; can use a tablet and large buttons but needs a simple board during the breakfast rush.
Quote: "Show me what to make next and let me mark it ready with one click."

These are fictional design personas, not interviewed individuals.
4. Must-have features
- A customer menu showing available products, descriptions, and prices.
- An order form with item quantities and a pickup name.
- Server-side validation that rejects empty orders and invalid quantities.
- An order confirmation showing the order number, items, and total.
- A kitchen board listing orders by arrival time and current status.
- Staff controls for received, preparing, ready, and picked up transitions.
- Order history that preserves completed orders across application restarts.
- A menu administration screen for staff to add or edit items and mark availability.
5. Not in this prototype
- Online payment processing or stored card information.
- SMS, email, or push notifications.
- A native iOS or Android mobile application.
- Loyalty points, rewards, or promotional codes.
- Delivery dispatch or driver tracking.
- Integration with a commercial point-of-sale or inventory system.
6. Questions and answers
Why is an out-of-scope list useful?
It gives the developer a clear boundary for time and effort and helps the client understand what will be demonstrated. It prevents expectations such as online payments or delivery from expanding the first prototype beyond the ordering and kitchen workflow. Excluded ideas can be considered for a later version.
Which persona matters most to the business owner, and why?
For this first prototype, Luis is the highest-priority operational persona because the kitchen must receive and complete every order reliably. A clear board reduces confusion and helps the cafe serve customers consistently during busy periods. Marta remains essential: a kitchen improvement is useful only if customers can place accurate orders and collect them easily.
7. Copilot interview
Prompt: Ask me five questions a product designer would ask before building an ordering app for a small Cuban cafe in Little Havana. Focus on customers, the current ordering process, kitchen staff, order status, and prototype scope. Ask the questions first and wait for my answers before suggesting solutions.
1. Customers
Question: Who are the main customers, and what devices or languages do they prefer when ordering?
Answer summary: Local residents and breakfast commuters use smartphones and prefer Spanish or English. Ordering should be simple and should not require an account.
2. Current ordering process
Question: How do customers order today, and where do delays, mistakes, or friction tend to happen?
Answer summary: Customers order at the counter, and paper tickets go to the kitchen. Busy periods create queues, unclear handwriting, misplaced tickets, and repeated status questions.
3. Kitchen staff
Question: Who receives and prepares orders, and what information or workflow would help them handle orders during busy periods?
Answer summary: Counter staff receive orders; kitchen staff prepare them. The board needs order numbers, items, quantities, pickup names, receipt times, and statuses, ordered from oldest to newest.
4. Order status
Question: Which order status updates should customers and staff see, and who should update each status?
Answer summary: Customers see their own order status; staff see all orders. New orders start as received. Kitchen staff update preparing and ready; counter staff mark picked up after handoff.
5. Prototype scope
Question: What should the first prototype cover - for example, pickup or delivery, payment or pay-at-pickup, and a limited or full menu?
Answer summary: Pickup only, payment at the counter, and a small sample menu of Cuban coffee, drinks, and pastries. Include ordering, confirmation/status, kitchen board, history, and basic menu administration. Exclude delivery, online payments, notifications, and loyalty rewards.

Copilot acknowledged the five responses and summarized the discovery brief. The answers describe the proposed class scenario, not field research.
8. AI log
Tool: GitHub Copilot Chat (Free)
Prompt: The five-question interview prompt in section 7.
Produced: Five discovery questions about customers, current ordering, kitchen staff, order status, and prototype scope; then a summary of the submitted responses.
Decision: Kept the interview structure and used its summary to review the proposal.
Reason: The interview clarified a pickup-only workflow, staff responsibilities, and prototype boundaries.

Tool: ChatGPT
Prompt: The assignment instructions, followed by a request to prepare it quickly and provide step-by-step help.
Produced: A proposal draft, fictional personas, scope lists, explanations, suggested interview answers, and document formatting.
Decision: Used as drafting support.
Reason: Helped organize the scenario and complete the interview. The original proposal draft preceded the Copilot interview and was reviewed afterward; the assignment asks for the final problem statement in the student's own words.
9. Repository
Use the existing egn475-cafe-valadares repository. The earlier hello Flask exercise used Valadares Cafe; the selected term project is Cafe Calle Ocho. This updated README still needs to be committed and pushed to main; publication of this revision has not been verified.