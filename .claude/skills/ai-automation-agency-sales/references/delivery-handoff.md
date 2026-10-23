# Delivery Handoff (sales → build)

The salesperson's job ends with a clean spec. Builders shouldn't have to re-ask the client anything.

## Recommended tooling
- **Workflows:** n8n, built with Claude using **czlonkowski/n8n-mcp** (lets Claude read node schemas, validate and deploy workflows) and **czlonkowski/n8n-skills** (expression syntax, node config, workflow patterns). Optionally EtienneLescot/n8n-as-code for version-controlled workflows per client.
- **Voice:** Vapi or Retell (or whatever the agency has standardized on). Keep one platform per agency to simplify support.
- **SMS/phone:** the agency's telephony provider or the client's CRM (e.g. GHL/LeadConnector), with A2P 10DLC registration done before launch in the US.

## Handoff spec template

```markdown
# Build spec — [Business] — [Offer]
Sold by: [rep] · Signed: [date] · Kick-off: [date] · Target live: [date]

## Outcome in one line
[e.g. "Every unanswered call to the main line gets a text within 60 seconds and a booking link; owner gets a summary SMS."]

## Triggers and flow
1. Trigger: [missed call on number X / form submit / after-hours call]
2. Action: [send SMS template #1 / voice agent answers]
3. Branches: [reply → book / no reply → follow-up at +1h, +1d / "stop" → opt out]
4. Hand-off to human: [when, how, to whom: phone/SMS/email]

## Knowledge for the agent (approved by client)
Hours · services · service area · prices (only if client approves stating them) · FAQs · things the agent must NOT answer → escalate

## Scripts and messages
[Every SMS/voice greeting, verbatim, with client approval date]
Greeting must disclose: "This is the automated assistant for [Business]."

## Integrations and access needed
[ ] Phone provider / number porting or forwarding
[ ] Calendar / booking tool
[ ] CRM
[ ] n8n instance (agency-hosted / client-hosted)
[ ] Voice platform account

## Compliance checklist (see compliance-risk.md)
[ ] Recording consent approach for the client's state(s)
[ ] SMS consent and opt-out handling ("STOP")
[ ] A2P 10DLC brand + campaign registration submitted
[ ] Client confirmed with their own advisor if in doubt

## Pilot criteria / acceptance tests
[From the proposal]

## Monitoring
Weekly check of failed runs, call transcripts sample, opt-outs; monthly report to client with real counts only.
```
