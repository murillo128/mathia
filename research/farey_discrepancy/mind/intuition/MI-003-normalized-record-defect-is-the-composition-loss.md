# MI-003 — Bounded normalized record defect closes every current one-step predecessor branch

**Evidence level:** exact through [FD-094](../../findings/FD-094-normalized-schur-energy-records-upgrade-frontier-carriers-to-fixed-occupation.md) for the exact lower transports and through [FD-095](../../findings/FD-095-bounded-record-defect-turns-the-source-head-into-an-amplitude-scale-predecessor.md) for the formerly terminal source-head branch. Existence of sufficiently sharp occupied packets with bounded defect, and uniform control through many predecessor steps, remain open.

For fixed `sigma>1/2`, normalize the complete Schur energy by

`F_sigma(N)=E_(N,1)/N^(2 sigma)`

and measure the parent's backward record defect by

`R_sigma(H)=max(1, sup_(2<=N<H) F_sigma(N)/F_sigma(H))`.

For every branch that already admits an exact lower mask at `C<H`, FD-094 shows that the gap between frontier-normalized size and fixed lower-state occupation is exactly priced by `R_sigma(H)`: if

`M_C/C^(2 sigma) >= (a-o(1)) F_sigma(H)`,

then

`M_C/E_(C,1) >= (a-o(1))/R_sigma(H)`.

FD-095 removes the only qualitatively different one-step branch. If the dyadic row-two/source-head value `S_H=|mathcal H(B_H)|` carries a fixed parent share, use the source's exact one-Lipschitz law instead of insisting on literal source preservation. Retreat by `h=floor(lambda S_H)` with fixed `0<lambda<1`, put `C=4(B_H-h)`, and reembed the nearby source value on the nonsquarefree row `4`. Then `C<H`, the source amplitude retains a `(1-lambda)` fraction, and bounded `R_sigma(H)` again upgrades the transported mass to a fixed occupation fraction of `E_(C,1)`.

On a sharp false-RH frontier the head backstep is not infinitesimal: `H-C >= H^(Theta-o(1))` while `C` remains comparable with `H`. The predecessor also inherits a bounded record defect, with a constant depending only on the parent's defect and the fixed transport parameters. The same inheritance is immediate for the other FD-094 branches.

Thus the current exact one-step statement has a single common hypothesis:

**sharp occupied parent + `R_sigma(H)=O(1)` => some genuinely lower sharp occupied state + bounded inherited record defect.**

The former source-head representability obstruction is no longer independent. The first residual is to couple the abundant sharp occupied packet family to bounded historical defect. False RH supplies infinitely many strict records of `F_sigma`, but that does not yet show that the occupied packet horizons hit records or even stay within a bounded factor of them.

A second, logically later residual appears only after one-step closure: the inherited constants can deteriorate under iteration. Odd-prime branches may contract multiplicatively, while a head step can descend only additively by `H^(Theta-o(1))`. An infinite or sufficiently long descent therefore needs a uniform invariant, recurrent return to fresh records, or another mechanism preventing occupation/defect constants from degrading with depth.

**Boundary.** FD-094--FD-095 do not prove a bounded-defect occupied sequence, a uniform multistep invariant, or the final false-RH contradiction. They do prove that, conditional on bounded record defect at the parent, no currently known local predecessor branch—including the source head—requires a separate representability theorem.
