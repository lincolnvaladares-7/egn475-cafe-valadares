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

1. **Given** my order has an item and my name contains at least one non-space character, **when** I submit it, **then** I receive an order number and a Received status.
2. **Given** my name is blank or contains only spaces, **when** I submit the order, **then** no order is created and the name field displays “Enter your name.”
3. **Given** my order is empty, **when** I submit it, **then** no order is created and the form displays “Add at least one item.”

### US-05 — Must
**As a** kitchen staff member, **I want** to view incoming orders, **so that** I can see what needs preparing.

1. **Given** a customer submits a valid order, **when** I open the kitchen board, **then** the order appears with its number, items and Received status.
2. **Given** no orders have been submitted, **when** I open the kitchen board, **then** an empty-state message appears without a fake order.

### US-06 — Must
**As a** kitchen staff member, **I want** to advance an order from Received to Preparing, **so that** I can show that work has started.

1. **Given** an order is Received, **when** I choose Start preparing, **then** its status becomes Preparing.
2. **Given** an order is already Ready, **when** I choose Start preparing, **then** its status remains Ready and the kitchen board displays “Only Received orders can be started.”

### US-07 — Should
**As a** kitchen staff member, **I want** to mark a Preparing order as Ready, **so that** customers can know when to collect it.

1. **Given** an order is Preparing, **when** I choose Mark ready, **then** its status becomes Ready.
2. **Given** an order is still Received, **when** I choose Mark ready, **then** its status remains Received and the kitchen board displays “Only Preparing orders can be marked ready.”

### US-08 — Could
**As a** customer, **I want** to check my order status using its order number, **so that** I know when to collect my food.

1. **Given** I enter the order number assigned to an existing order, **when** I request its status, **then** the page displays that order’s number and exactly one current status: Received, Preparing or Ready.
2. **Given** I enter an order number that does not match an existing order, **when** I request its status, **then** the page displays “Order not found.”
3. **Given** the order number field is empty or contains only spaces, **when** I request a status, **then** no lookup is performed and the field displays “Enter an order number.”

## Reflection questions

**1. Which story did you split into smaller stories, and why?**
No story was identified as too large in the INVEST review, so no story was split.

**2. Which story was hardest to write acceptance criteria for? What made it hard?**
US-06 was the hardest because status changes require defining both an allowed transition and a rejected transition. The criteria distinguish Received → Preparing from an invalid Ready → Preparing change.

## AI Log

The INVEST review found no stories too large. I accepted all four suggestions to make vague or underspecified acceptance outcomes observable and testable:

| Finding | Decision | Why the change improves testability |
| --- | --- | --- |
| US-04 did not define what counts as a blank name or what happens for invalid submissions. | Accepted | Whitespace-only names and empty orders have explicit validation text, and the criteria state that no order is created. |
| US-06 said an invalid change is rejected without specifying user-visible feedback. | Accepted | The Ready status must remain unchanged, and the board must display an exact message that can be checked. |
| US-07 did not state the resulting status or observable response when skipping a status step. | Accepted | The Received status must remain unchanged, and the board must display an exact rejection message. |
| US-08 used “valid” and “helpful” without defining the cases or outcomes. | Accepted | The criteria define an existing order number, the possible displayed statuses, the not-found result, and the empty-input result with exact messages. |

## Repository submission checklist

- Save this backlog as `USER_STORIES.md` at the repository root.
- Verify the AI Log records the review findings, decisions and reasons.
- Commit and push to `main`.
- Submit the repository URL and the matching PDF to Online Campus.
