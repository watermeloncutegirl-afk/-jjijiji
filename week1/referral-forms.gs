/**
 * Creates two Google Forms and links their responses into this spreadsheet:
 *   1. "Partner sign-up" – people join your referral program and accept the terms.
 *   2. "Refer a client"  – partners submit a business that needs a website / AI automation.
 *
 * How to run (one time):
 *   1. Upload lead-tracker.xlsx to Google Drive → open with Google Sheets
 *      (or in Sheets: File → Import → Upload → "Replace spreadsheet").
 *   2. Extensions → Apps Script → delete the sample code → paste this whole file → Save.
 *   3. Edit the CONFIG block below (your name, email, terms link).
 *   4. Choose "createReferralForms" in the toolbar → Run → approve the permissions.
 *   5. Form links appear in the Settings tab (and in View → Logs).
 *
 * Each form gets its own response tab ("Form Responses 1", "Form Responses 2").
 * Rename them to "Partner signups" and "Referrals" if you like.
 */

var CONFIG = {
  yourName: 'YOUR NAME',
  businessName: 'YOUR BUSINESS',
  contactEmail: 'you@example.com',
  // Paste the public link to your referral terms (e.g. a Google Doc shared "Anyone with the link").
  termsUrl: 'https://docs.google.com/…',
  commissionSummary: '15% of the first project (max £750) + 10% of monthly retainers for 6 months + £150 bonus on your 3rd qualifying deal.'
};

function createReferralForms() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var signup = buildSignupForm_(ss.getId());
  var referral = buildReferralForm_(ss.getId());

  var settings = ss.getSheetByName('Settings') || ss.insertSheet('Settings');
  settings.appendRow(['Partner sign-up form (share this)', signup.getPublishedUrl()]);
  settings.appendRow(['Partner sign-up form (edit)', signup.getEditUrl()]);
  settings.appendRow(['Refer-a-client form (send to partners)', referral.getPublishedUrl()]);
  settings.appendRow(['Refer-a-client form (edit)', referral.getEditUrl()]);

  Logger.log('Partner sign-up: ' + signup.getPublishedUrl());
  Logger.log('Refer a client: ' + referral.getPublishedUrl());
}

function buildSignupForm_(spreadsheetId) {
  var form = FormApp.create(CONFIG.businessName + ' – Referral Partner Sign-up');
  form.setDescription(
    'Know businesses that need a website or AI automation (chatbots, booking, lead follow-up)? ' +
    'Refer them to ' + CONFIG.yourName + ' and earn: ' + CONFIG.commissionSummary + '\n\n' +
    'Full terms: ' + CONFIG.termsUrl + '\nQuestions: ' + CONFIG.contactEmail);
  form.setCollectEmail(true);

  form.addTextItem().setTitle('Full name').setRequired(true);
  form.addTextItem().setTitle('Business / job title (if any)');
  form.addTextItem().setTitle('Country').setRequired(true);
  form.addMultipleChoiceItem().setTitle('Which best describes you?')
      .setChoiceValues(['Past client', 'Accountant / bookkeeper', 'Marketer / agency', 'Designer',
                        'Photographer', 'Coach / consultant', 'Developer', 'Printer / sign shop', 'Friend / network'])
      .showOtherOption(true).setRequired(true);
  form.addMultipleChoiceItem().setTitle('How should we pay your commission?')
      .setChoiceValues(['Bank transfer', 'PayPal', 'Wise']).showOtherOption(true).setRequired(true);
  form.addCheckboxItem().setTitle('Terms')
      .setHelpText('Read them here: ' + CONFIG.termsUrl)
      .setChoiceValues(['I have read and accept the referral partner terms, including telling people I recommend that I may earn a referral fee.'])
      .setRequired(true);

  form.setConfirmationMessage('Thanks for joining! You\'ll get your partner code by email within 24 hours.');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, spreadsheetId);
  return form;
}

function buildReferralForm_(spreadsheetId) {
  var form = FormApp.create(CONFIG.businessName + ' – Refer a Client');
  form.setDescription(
    'Submit a business that needs a website or AI automation. The submission time is your proof of referral ' +
    '(first referral wins; 90-day window). Commission is paid 30 days after the client\'s payment clears.');
  form.setCollectEmail(true);

  var codeCheck = FormApp.createTextValidation()
      .setHelpText('Use the partner code you were given, e.g. JANE01')
      .requireTextMatchesPattern('^[A-Za-z0-9]{3,12}$').build();
  form.addTextItem().setTitle('Your partner code').setValidation(codeCheck).setRequired(true);
  form.addTextItem().setTitle('Client name').setRequired(true);
  form.addTextItem().setTitle('Client business name').setRequired(true);
  form.addTextItem().setTitle('Client email or phone').setRequired(true);
  form.addTextItem().setTitle('Client website or social link (if any)');
  form.addCheckboxItem().setTitle('What do they need?')
      .setChoiceValues(['New website', 'Website redesign / fixes', 'AI chatbot', 'Booking / scheduling automation',
                        'Lead follow-up / CRM automation', 'Not sure yet'])
      .showOtherOption(true).setRequired(true);
  form.addMultipleChoiceItem().setTitle('Rough budget (if known)')
      .setChoiceValues(['Under £500', '£500–£1,500', '£1,500–£5,000', '£5,000+', 'Don\'t know']);
  form.addParagraphTextItem().setTitle('Anything else I should know? (timeline, pain points)');
  form.addCheckboxItem().setTitle('Consent')
      .setChoiceValues(['The client knows I\'m passing on their details and is happy to be contacted.',
                        'I have told the client I may earn a referral fee.'])
      .setRequired(true);

  form.setConfirmationMessage('Got it – thank you! I\'ll contact them within 1 business day and keep you posted.');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, spreadsheetId);
  return form;
}
