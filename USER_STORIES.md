# Café Calle Ocho — User Stories and Acceptance Criteria

**Course:** EGN 475 — Week 2, Assignment 1
**Student:** Lincoln Guimaraes Valadares
**Project:** Café Calle Ocho Flask prototype

## Backlog

Personas: Café customer and kitchen staff member. Priorities: Must (6), Should (1), Could (1).

### US-01 — Must
**As a** customer, **I want** to view the café menu with prices and availability, **so that** I can decide what to order.

1. **Given** the menu has available items, **when** I open the menu, **then** each item displays its name, price and availability.
2. **Given** an item is sold out, **when** I view the menu, **then** the item is marked unavailable and cannot be selected.

### US-02 — Must
**As a** customer, **I want** to add an available menu item to my order, **so that** I can build a meal.

1. **Given** an item is available, **when** I select Add to order, **then** the item appears in my order with quantity one.
2. **Given** an item is sold out, **when** I try to add it, **then** the order remains unchanged and I see an availability message.

### US-03 — Must
**As a** customer, **I want** to change quantities in my order, **so that** I can correct my selections before checkout.

1. **Given** my order contains an item, **when** I increase its quantity, **then** the quantity and total update.
2. **Given** my order contains an item with quantity one, **when** I decrease its quantity, **then** the item is removed and the total updates.

### US-04 — Must
**As a** customer, **I want** to submit an order with my name, **so that** the café can prepare the correct order.

1. **Given** my order has an item and my name is entered, **when** I submit it, **then** I receive an order number and a Received status.
2. **Given** my name is blank or my order is empty, **when** I submit it, **then** submission is blocked with a clear message.

### US-05 — Must
**As a** kitchen staff member, **I want** to view incoming orders, **so that** I can see what needs preparing.

1. **Given** a customer submits a valid order, **when** I open the kitchen board, **then** the order appears with its number, items and Received status.
2. **Given** no orders have been submitted, **when** I open the kitchen board, **then** an empty-state message appears without a fake order.

### US-06 — Must
**As a** kitchen staff member, **I want** to advance an order from Received to Preparing, **so that** I can show that work has started.

1. **Given** an order is Received, **when** I choose Start preparing, **then** its status becomes Preparing.
2. **Given** an order is already Ready, **when** I try to start preparing it, **then** the status stays Ready and the invalid change is rejected.

### US-07 — Should
**As a** kitchen staff member, **I want** to mark a Preparing order as Ready, **so that** customers can know when to collect it.

1. **Given** an order is Preparing, **when** I choose Mark ready, **then** its status becomes Ready.
2. **Given** an order is still Received, **when** I try to mark it Ready, **then** the system rejects the skipped step.

### US-08 — Could
**As a** customer, **I want** to check my order status using its order number, **so that** I know when to collect my food.

1. **Given** I enter a valid order number, **when** I request its status, **then** the current status is displayed.
2. **Given** I enter an unknown or empty order number, **when** I request its status, **then** a helpful not-found or required-field message appears.

## Reflection questions

**1. Which story did you split into smaller stories, and why?**
The initial broad idea, "As kitchen staff, I want to manage orders," was divided into US-05 (view incoming orders), US-06 (start preparing), and US-07 (mark ready). Each now has one clear behavior, can be developed independently, and has observable acceptance tests.

**2. Which story was hardest to write acceptance criteria for? What made it hard?**
US-06 was the hardest because status changes require defining both an allowed transition and a rejected transition. The criteria distinguish Received → Preparing from an invalid Ready → Preparing change.

## AI review log

**Review prompt to paste into Copilot Chat:**

> Here are my user stories for a Flask prototype. Check each one against INVEST and tell me which are too big, vague or not testable. Do not rewrite them; list problems only.

**Review status:** Pending actual Copilot review. The notes below are a preliminary self-review, not Copilot output. Replace or supplement them with Copilot’s real feedback before submission.

| Potential issue (self-review) | Decision | Reason |
| --- | --- | --- |
| “Manage orders” combines several tasks | Accept | Split into US-05, US-06 and US-07 for independent testing. |
| Menu availability might depend on inventory integration | Reject for this prototype | A simple available/sold-out flag is enough for a testable mockup. |
| Status lookup could expand into notifications | Reject scope expansion | US-08 is deliberately limited to a manual lookup. |

**Copilot findings and final decisions:** Add the exact issues Copilot flags, mark each Accepted or Rejected, and explain why. Do not claim the preliminary notes are Copilot findings.

## Repository submission checklist

- Save this backlog as `USER_STORIES.md` at the repository root.
- Run the review prompt in Copilot Chat and complete the AI log with its actual findings.
- Commit and push to `main`.
- Submit the repository URL and the matching PDF to Online Campus.
