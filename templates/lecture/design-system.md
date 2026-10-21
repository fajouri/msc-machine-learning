# Proposed academic lecture design

The exact baseline tokens are in [design.json](design.json). This is an original design proposal for M5, pending professor review. No university logo, branding or institutional template is assumed.

## Screen and layout

Use a 16:9 canvas, approximately 13⅓ × 7½ inches, with a 0.5-inch safe margin. The rounded width token is equivalent within 0.001 inch. Use a white background, dark navy text and dark teal accents. Body and labels must reach a proposed minimum 4.5:1 contrast; meaningful graphical boundaries should reach 3:1. Do not rely on colour alone. These are design targets, not a claim of certified accessibility.

Use Arial as the proposed family, subject to actual font availability and embedding/substitution checks during build. Sizes are points: cover 44, slide title 36, body 24, equations 28, figure labels/captions 20, citation footer 18. A footer contains a short citation key/locator and slide number; full attribution belongs in notes and the reference section. Keep all footers inside the safe margin. Split dense content across slides rather than reducing text below these baselines. Long locators may continue on a reference slide but must remain traceable from the originating slide.

Use one main claim or question per slide. Place the title at the top, content below and citation/footer at the bottom without overlap. Prefer a single content column; a comparison may use two aligned columns with a clear reading order. Reserve enough room for equations and axis labels. Avoid decorative imagery, animation-dependent explanations, three-dimensional charts and screenshot text. A ten-type scaffold is a vocabulary, not a required slide sequence or count.

## Slide vocabulary

| Type | Visible content | Public notes and review focus |
| --- | --- | --- |
| opening | Session, problem and scope | Prerequisites and motivation |
| outcomes | Exact relevant approved LO wording | Explain links to activities without redefining outcomes |
| concept | Definition, assumptions, contrast or counterexample | Explain mechanisms and boundary cases |
| equation | One derivation segment and symbol definitions | Intermediate reasoning, dimensions and interpretation |
| comparison | Common criteria applied to methods | Trade-offs, evidence, assumptions and uncertainty |
| worked_example | Original teaching example and interpretable result | Reproducible method; never answer an independent task |
| figure | Editable evidence with axes, units and caption | Generation details, limitations and accessible explanation |
| activity | Formative question, timebox and participation route | Online/campus facilitation and outage fallback; no solution |
| synthesis | Main findings and limits linked to LOs | Transfer to another problem and remaining uncertainty |
| references | Verified full references and locators | Rights and provenance; TODOs prevent completion |

Every slide includes a stable ID, type, title, purpose, LO links, visible body, equations/figures/citations arrays and public notes. Empty arrays mean no such content is declared. Each record remains visible in the Markdown/Word source to make review possible.

## Mathematical reasoning

Define symbols before use, including domains, shapes, units and index ranges. Distinguish scalars, vectors and matrices consistently (italic scalar, bold lowercase vector, bold uppercase matrix); name any exceptions. Distinguish random variables from observations and population quantities from empirical estimates. Define training/validation/test partitions before introducing fitted preprocessing or evaluation claims.

Store each equation as editable LaTeX source plus a spoken form. Record symbols/dimensions, assumptions, derivation, interpretation and limitations in separate fields. Explain intermediate steps and why the objective/update is appropriate; include uncertainty, numerical stability and failure cases when relevant. Separate statistical bias from societal bias. Do not insert decorative mathematics into a session merely to fill the template.

Future Word/PowerPoint builds must use editable equation objects where supported and preserve the original source. Do not silently rasterise unsupported notation. Flag the expression for a human conversion decision and compare subscripts, superscripts, Greek symbols, minus signs, sums, fractions and alignment against the source after rendering. A string validator cannot establish mathematical correctness.

## Figures and reproducibility

Use native charts with embedded synthetic/publicly permitted data, native tables, or grouped native shapes/connectors. Diagrams need labelled nodes, explicit arrow meaning and reading order. Keep labels editable. Figure records include origin, source ID, editable form, reproduction details, caption, alt text, reading order and encoding beyond colour. For original assets, use `origin: original` and `source_id: original`; this declaration is subject to human review.

Record the generating script/data revision, seed where stochastic, dependency versions, units, preprocessing and uncertainty in `data_and_reproduction`. Explain any absence of these items instead of inventing a seed or result. Preserve data tables for chart recreation. Third-party figures require verified bibliography keys and matching citation records; register actual reuse in the existing ledger and obtain asset-specific clearance. Citation alone does not permit copying. Do not embed textbook pages or external data downloads in the source scaffold.

## Citations and notes

Each citation contains the existing registry `source_id`, repository-relative destination `artifact`, verified `locator` and visible `attribution`. Unknown sources must undergo the established bibliography workflow, not be guessed. Locators not yet verified remain TODO in drafts. Register each actual source/destination use, including future binaries, in `references/citation-usage.json`. Complete-mode matching is only for declared uses and does not establish full coverage or rights clearance.

Notes belong in the actual PowerPoint speaker-notes field during a future build, not outside the slide canvas. Use the seven named sections from the source schema: explanation, reasoning, timing, participation online, participation campus, fallback and transition. Place full citations with the explanation. Notes may be distributed with the deck and must be safe for students. Exclude instructor-only exercise answers, exam questions/keys, student details and private correspondence, including comments and hidden slides.

## Accessibility and delivery checks

Provide meaningful alt text describing a figure's message, trends and necessary values, rather than its appearance alone. Use markers, line patterns and direct labels as well as colour. Order objects title → body/figure → caption → citation. Use descriptive links and built-in heading/list/table semantics. Describe equations and visual changes aloud; provide equivalent source text. Avoid flashing, essential animations or time-limited visual cues.

Future visual QA must check every slide at 1280×720 and full screen, including Greek/mathematical glyphs, overlap, clipping, chart labels, reading order and captions. Test a real projector from the back of the room and a Google Meet share on a typical laptop. Record display/share conditions and reviewer findings; these tests have not run. Human review must confirm screen-reader navigation and useful alt text. Slides alone do not replace accessible activity instructions or the approved delivery plan.

## Word source mapping

The same `lecture.schema.json` defines the Word source, not an independent prose schema. The Markdown is a reviewable intermediate, not a DOCX. A later converter must apply the following semantic mapping, preserving content and ordering. Nested JSON records in the intermediate must become labelled paragraphs/tables, not raw code blocks in the final Word document.

| Source element | Word mapping |
| --- | --- |
| Document title | Title style, black, no border/underline |
| Lecture framing and slide ID/title | Heading 1, 20 pt, black |
| Field/notes section names | Heading 2, 16 pt, black |
| Nested record labels | Heading 3, 13 pt, black |
| Body and notes | Normal, 12 pt; labelled public notes after each slide |
| Equation | Editable equation, 14 pt baseline plus spoken form and definitions |
| Figure | Editable source retained, caption 11 pt, alt text attached |
| Citation | Traceable attribution beside use and full reference section |

Use A4 portrait with 25 mm margins, real page numbers, heading keep-with-next, and repeating table headers. Avoid orphan headings, split equations and separated captions. Inspect every rendered page before delivery. No DOCX style, page count or pagination success is claimed by these source rules.
