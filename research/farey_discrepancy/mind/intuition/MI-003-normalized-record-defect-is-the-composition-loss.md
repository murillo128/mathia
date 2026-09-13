# MI-003 — Source-record slowdown supplies bounded defect; the remaining loss is depth growth

**Evidence level:** exact through [FD-094](../../findings/FD-094-normalized-schur-energy-records-upgrade-frontier-carriers-to-fixed-occupation.md) for repairable lower transports, [FD-095](../../findings/FD-095-bounded-record-defect-turns-the-source-head-into-an-amplitude-scale-predecessor.md) for the formerly terminal source-head branch, and [FD-096](../../findings/FD-096-source-record-doubling-slowdown-forces-sharp-occupied-bounded-defect-horizons.md) for existence of infinitely many sharp occupied bounded-defect entry states under a false-RH frontier. Uniform control through a depth growing with the starting scale remains open.

For fixed `1/2<sigma<Theta`, normalize the complete Schur energy by

`F_sigma(N)=E_(N,1)/N^(2 sigma)`

and measure the parent's backward record defect by

`R_sigma(H)=max(1, sup_(2<=N<H) F_sigma(N)/F_sigma(H))`.

FD-094 shows that `R_sigma(H)` is exactly the price that turns a frontier-sized transported carrier into a fixed lower-state occupation fraction. FD-095 removes the qualitatively different dyadic source-head atom: source Lipschitz coherence permits an amplitude-scale backward move and four-adic reembedding, again with bounded inherited defect whenever the parent defect is bounded.

FD-096 closes the previously missing entry theorem without intersecting two unrelated packet families. For the normalized physical source record

`P_sigma(X)=max_(n<=X) |mathcal H(n)|/n^sigma`,

the global power frontier forces infinitely many strict records with bounded doubling, for example `P_sigma(2X)<=2P_sigma(X)`. Set `H=4X`. Every complete Schur row `r>=2` then samples the source at an argument at most `2X`, while the nonsquarefree row `r=4` samples the sharp record value at `X` exactly. The same two-scale source envelope yields simultaneously

`E_(H,1)=H^(2Theta+o(1))`, `U_(H,1)/E_(H,1)>=c_sigma>0`, and `R_sigma(H)<=C_sigma`.

Thus the old coupling problem “find a sharp occupied packet with bounded historical defect” is no longer live under false RH. Infinitely many such packets are forced directly from source records, and every one admits a genuine lower sharp occupied bounded-defect continuation by FD-094--FD-095.

The remaining obstruction is **iteration depth**. The inherited occupation and defect constants can deteriorate at each predecessor step. Odd-prime repairs may contract multiplicatively, whereas a source-head move can retreat only additively by `H^(Theta-o(1))`. FD-096 does imply chains of every fixed finite depth by starting sufficiently far out, but it does not give a chain whose depth tends to infinity with the starting horizon.

A final contradiction therefore needs a depth-uniform invariant, a recurrent return to fresh source/energy records, or another quantitative mechanism showing that accumulated transport losses grow slowly enough relative to the number and geometry of predecessor steps. Re-proving one-step representability or bounded-defect entry no longer attacks the active boundary.

**Boundary.** FD-096 is conditional on the false-RH frontier `Theta>1/2` and a fixed `sigma in (1/2,Theta)`. It proves neither a depth-uniform descent nor a contradiction to false RH. The convergence threshold `sigma>1/2` is structural in the Schur-row sum used to control the complete history.
