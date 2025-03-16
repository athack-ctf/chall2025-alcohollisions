# @HACK 2025: Alcohollisions

> Authored by [Chit Chit](https://github.com/littleSquid00).

- **Category**: `Crypto`
- **Value**: `100 points`
- **Tags**: `http`

> Professor Gilbert Winestein is a renowned cybersecurity expert... and an even bigger wine enthusiast!
> His prized wine collection features exclusive bottles from the renowned vineyard Château AtHack.
> Every time he adds a new bottle, he struggles to check if it's already in his collection because comparing all the labels takes forever.
> To speed up the process, Winestein's friends suggested a clever hack: record the MD5 hash of each label.
> Since MD5 hashes are short, it would make his collection faster to manage.
> 
> But you, a sharp and curious student of his, notice a potential flaw.
> What if two labels from different bottles accidentally produce the same MD5 hash? Winestein might think they're duplicates and toss out a unique wine!
> 
> To convince him, you decide to demonstrate how two different labels can have the same MD5 hash but different SHA-256 hashes. Use this information to teach him why relying on MD5 alone might not be the best choice for such a prized collection.
> 

## Files
- **[Download: christmaslabel.jpg](https://github.com/athack-ctf/chall2025-alcohollisions/raw/refs/heads/main/offline-artifacts/christmaslabel.jpg)**
- **[Download: easterlabel.jpg](https://github.com/athack-ctf/chall2025-alcohollisions/raw/refs/heads/main/offline-artifacts/easterlabel.jpg)**
- **[Download: halloweenlabel.jpg](https://github.com/athack-ctf/chall2025-alcohollisions/raw/refs/heads/main/offline-artifacts/halloweenlabel.jpg)**

## Access a dockerized instance

Run challenge container using docker compose
```
docker compose up -d
```
Open below URL on your browser
```
http://localhost:52002/
```
<details>
<summary>
How to stop/restart challenge?
</summary>

To stop the challenge run
```
docker compose stop
```
To restart the challenge run
```
docker compose restart
```

</details>


## Reveal Flag

Did you try solving this challenge?
<details>
<summary>
Yes
</summary>

Did you **REALLY** try solving this challenge?

<details>
<summary>
Yes, I promise!
</summary>

Flag: `ATHACKCTF{y0uar3aSharpStud3nt}`

</details>
</details>


---

## About @HACK
[@HACK](https://athackctf.com/) is an annual CTF (Capture The Flag) competition hosted by [HEXPLOIT ALLIANCE](https://hexploit-alliance.com/) and [TECHNATION](https://technationcanada.ca/) at Concordia University in Montreal, Canada.

---
[Check more challenges from @HACK 2025](https://github.com/athack-ctf/AtHackCTF-2025-Challenges).