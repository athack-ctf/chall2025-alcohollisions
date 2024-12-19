# Professor Winestein and his wine collections

> This challenge is a hash collision challenge and is about finding a file with the same MD5 Hash as a given file. It requires participants to learn about hash collision attacks because it is not doable without them.

## Type

- [x] **ON**line

## Designer(s)

- Little Squid

## Description

Participants will be given three images. Those images are of wine labels. The participants will be asked to provide a file with the same MD5 hash as one of the three given files. The participants will have to recognize which of the files was generated as a result of a hash collision attack, and how that collision works, so as to exploit it.

Educational Goals: (1) Participants will gain an understanding of hash collisions, specifically MD5 vulnerabilities, and how attackers exploit these weaknesses. (2) Participants will improve their ability to analyze cryptographic artifacts (e.g., files with similar hashes) and understand the implications of weak hash functions in real-world applications.

Skills Test:(1) Participants will show understanding of how a specific hash collision attack works by identifying the target file and generating a valid collision file with the same MD5 hash. (2) Participants will use analytical and critical thinking skills to deduce which file corresponds to a hash collision and what hash collision attack was used to generate that file. (3) Participants will showcase proficiency with tools for computing MD5 hashes.
**IMPORTANT:** This description will **NOT** be shared with participants.

## Category(ies)

- `stegano`
- `crypto`

---

# Project Structure

## 1. HACKME.md

- **[HACKME.md](HACKME.md)**: A teaser or description of the challenge to be shared with participants (in CTFd).

## 2. Source Code

- **[source/README.md](source/README.md)**: Comprehensive instructions on how to have a running instance of your
  challenge from the source.
  If your project includes multiple subprojects, please consult us (Anis and Hugo).
- **[source/\*](source/)**: Your source code.

## 3. Offline Artifacts [OPTIONAL]

> **NOTE:** This directory is optional for online challenges. However, if offline artifacts need to be provided as well,
> they should be placed here.

- **[offline-artifacts/\*](offline-artifacts/)**: All files intended to be downloaded by participants
  (e.g., a flagless version of the running binary executable of a pwn challenge).
  For large files (exceeding 100 MB), please consult us (Anis and Hugo).

## 4. Solution

- **[solution/README.md](solution/README.md)**: A detailed writeup of the working solution.
- **[solution/FLAGS.md](solution/FLAGS.md)**: A single markdown file listing all (up-to-date) flags.
- **[solution/\*](solution/)**: Any additional files or code necessary for constructing a reproducible solution for the
  challenge (e.g., `PoC.py`, `requirement.txt`, etc.).

## 5. Dockerization

> **NOTE:** For deployment on @Hack's infrastructure, online challenges must be containerized.
> However, this requirement does not apply during the early stages of challenge development, so do not hesitate to start
> building your online challenge if you are unfamiliar with containerization.
> We (Anis and Hugo) will take care of it.

- **[source/Dockerfile](source/Dockerfile)**: Needed for building a containerized image of the online challenge.
- **[source/docker-compose.yml](source/docker-compose.yml)**: Needed for a configuration-free run of the online
  challenge
