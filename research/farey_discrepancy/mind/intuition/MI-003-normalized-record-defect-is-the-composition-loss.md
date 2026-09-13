# MI-003 — Normalized record defect is the remaining composition loss

**Evidence level:** exact through [FD-094](../../findings/FD-094-normalized-schur-energy-records-upgrade-frontier-carriers-to-fixed-occupation.md) for every currently repairable repeated-prime channel. The existence of occupied frontier packets with bounded record defect, and the separate row-two/source-head obstruction, remain open.

For fixed `sigma>1/2`, normalize the complete Schur energy by

`F_sigma(N)=E_(N,1)/N^(2 sigma)`

and measure how far a parent horizon `H` lies below its own previous record by

`R_sigma(H)=max(1, sup_(2<=N<H) F_sigma(N)/F_sigma(H))`.

If an exact lower transport produces a mask at `C<H` with

`M_C/C^(2 sigma) >= (a-o(1)) F_sigma(H)`,

then the same normalization of the complete lower state gives immediately

`M_C/E_(C,1) >= (a-o(1))/R_sigma(H)`.

Thus the old gap between “full frontier exponent” and “fixed occupation” is not an unspecified mask-versus-state defect. **For the repairable channels it is exactly priced by the backward normalized-energy record defect of the parent.** At a true `F_sigma` record, `R_sigma(H)=1`, so odd repeated-prime transport, the eligible dyadic half-scale branch, and the dyadic nonhead repairs all land in genuinely lower states with a fixed nonsquarefree occupation fraction.

Under false RH, `F_sigma` is unbounded for every `1/2<sigma<Theta`, so infinitely many strict records exist. What is not proved is that the abundant occupied near-frontier packets meet those records, or even have `R_sigma(H)=O(1)`. A persistent composition loss would therefore have to manifest as a concrete global separation: every useful occupied packet horizon would sit increasingly far below an earlier normalized-energy peak.

The row-two/source-head atom is different. It is not a lower-state mask inequality of the normalized form above, so record comparison does not lower it by relabeling. The two surviving gates are now sharply distinct: couple occupied packets to bounded record defect, or rule out persistent concentration on the single source-head atom.

**Research consequence.** Stop treating composition strength as a generic exponent problem. For repairable channels, test the scalar historical quantity `R_sigma(H)` along the actual occupied packet sequence. Exact recordhood is unnecessary; any uniform bound already restores fixed occupation.

**Boundary.** This does not prove such a bounded-defect sequence exists, does not repair the source-head atom, and does not itself produce the final false-RH contradiction.
