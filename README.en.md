# Piankouyu Boshi’s Livestream Notes

[简体中文](README.md) · **English**

This independent archive documents how the Chinese livestream creator Piankouyu Boshi (偏口鱼博士, often called 鱼博) answers viewers’ questions. The session notes preserve the order of the conversation. The topic chapters bring together answers from different dates. You can look up an answer, then jump to the recording to hear the follow-up that changed it. The notes and recordings are in Chinese.

**Start with a coconut.** When Piankouyu called coconut water expensive, a viewer from Hainan pushed back. He gave two examples. He could see paying five yuan for a coconut because you like the taste. He wouldn’t pay twenty or thirty on the promise that it would lighten your skin. The session preserves the exchange. The shopping chapter uses it to explore what someone is actually paying for. [Read the exchange and play the clip](sessions/2026-10-31.md#at-1522) · [Read the shopping notes](knowledge/shopping.md#coconut-price)

## Install in Codex

`piankouyu` is a standalone Skill that bundles the Q&As, topic chapters, and notes on the host’s speaking style. Paste the following line into a **Codex chat** to install it. [Browse the Skill directory](skills/piankouyu/)

```text
$skill-installer Install the Skill from https://github.com/l-s-c/piankouyu-notes/tree/main/skills/piankouyu
```

Once installed, try the following in your next message. The Skill paraphrases the host’s answers in the first person and links to the relevant timestamps.

```text
$piankouyu Can tofu count as the staple food in a meal? Compare Piankouyu’s September and October answers and link to both timestamps.
```

**Manual install from an existing checkout.** On macOS or Linux, open a terminal at the repository root and run the two lines below. The copy is skipped if a skill with the same name is already present.

```sh
piankouyu_dir="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$piankouyu_dir" && test ! -e "$piankouyu_dir/piankouyu" && cp -R skills/piankouyu "$piankouyu_dir/"
```

If the installer reports that the destination already exists, move the old `piankouyu` folder it identifies outside your skills directory as a backup, then run the install prompt again.

## Read a session from start to finish

These three public recordings from 2026 were covered from the opening seconds of each file to the sign-off. Together they contain **618 viewer questions and follow-ups**. Monologues and announcements are listed separately.

| Recording | Duration | Questions and follow-ups | What came up |
| --- | --- | ---: | --- |
| [February 28](sessions/2026-02-28.md) | 1:01:47 | 169 | Selenium-enriched eggs, and how his answer changed when a parent clarified that a child was three years old rather than three weeks old |
| [September 30](sessions/2026-09-30.md) | 1:20:48 | 246 | Broth in a lab versus soup at dinner, and why he asked what a student’s math test was scored out of |
| [October 31](sessions/2026-10-31.md) | 1:06:18 | 203 | Rice purée for someone who cannot chew, coconut prices in Hainan, and what parents can do while a child studies |

## Browse by question, topic, or date

| What are you looking for? | Where to start |
| --- | --- |
| An answer to a specific question | The index has 340 numbered entries. Some also appear in the three session notes. [Q&A index](dialogues.md) |
| His views on a subject | Chapters cover nutrition, eating habits, shopping, exercise, sleep, education, and family life. [Topic guide](knowledge/README.md) |
| A recording to watch | The calendar lists 268 recordings across 170 dates, with same-day versions side by side. A separate guide groups 29 short clips by topic. [Replay calendar](recordings.md) · [Short clips](clips.md) |
| The context behind a memorable line | Find the question behind his *Three Kingdoms* analogy about eggs and sea cucumbers, or the irreverent nickname he gave durian. [Speaking style and clips](voice.md) |
| A way to check a fan summary | Compare Douyin videos, Bilibili replays and clips, screenshots of Xiaohongshu notes, and viewer write-ups. Each source entry explains what could be verified. [Source index](sources.md) · [Xiaohongshu notes](xiaohongshu.md) · [Fan summaries and recordings](posts.md) |

## How to read and contribute

Answers are **first-person paraphrases**. The full-session notes distinguish questions the host read aloud from questions reconstructed from his reply. Follow the timestamp for his exact words. On health topics, **editorial notes** (编注) identify independent guidance and explain where it differs from the livestream answer.

To suggest a correction or a new entry, include the video link, timestamp, and passage. If he answered differently on another day, both clips help readers see which detail changed. The project also documents how other archives turn a public figure’s views into usable answers. [Notes on persona Skills](editing/persona-references.md)

After editing the Q&As or topic chapters, maintainers can refresh the bundled notes from the repository root with `python3 tools/sync-skill-references.py`. Add `--check` to verify that the bundle is in sync before committing.
