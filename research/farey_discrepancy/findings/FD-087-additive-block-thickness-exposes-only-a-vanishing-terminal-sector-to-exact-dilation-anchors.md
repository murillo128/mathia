# FD-087 — additive block thickness exposes only a vanishing terminal sector to exact dilation anchors

**Status:** `EXACT-DERIVED + FALSE-RH-FRONTIER + UNIFORM-DILATION-EMBEDDING + TERMINAL-SECTOR-CAPACITY + NEGATIVE/OBSTRUCTION + INTER-BLOCK-COMPOSITION-BOUNDARY`.

`FD-086` leaves a very specific inter-block question. Inside every near-frontier occupied block the complete signed Jordan state is asymptotically frozen, but different blocks may occur on multiplicatively incompatible scales. A natural way to use the additive thickness from `FD-084` is to select horizons in separated blocks that share a divisor `a`, send both states to a common multiple, and use the exact lower-horizon dilation copy from `FD-034`/`FD-067` as a common anchor.

There is an exact positive statement and a sharp negative one. The positive statement is that integer dilation is **uniformly well conditioned at the full Jordan-vector level for every dilation factor**, not only for nonsquarefree factors: a state at horizon `H` can be recovered from its canonical coordinate copy inside the state at `qH` with condition number at most `sqrt(zeta(2))`, independently of `q`. Thus an arbitrarily large least common multiple does not itself destroy the raw lower-horizon state.

The negative statement is that the additive blocks of `FD-084` can force common divisors only at scales no larger than their block length. On a false-RH near-frontier block of length

\[
L_H=H^{\Theta-\delta},
\qquad \Theta>\frac12,
\tag{1}
\]

**the entire Jordan sector that can contain exact dilation copies of all anchors `a<=L_H` has vanishing normalized energy**. More precisely, after choosing the near-frontier seed with an arbitrarily small fixed energy loss `kappa>0`, uniformly for every horizon `N` in the block,

\[
\boxed{
\frac{\|Q_{N,L_H}V_{N,D}\|_2^2}{E_{N,D}}
\ll H^{-c_{\Theta,\delta}}
\longrightarrow0,
}
\tag{2}
\]

where `Q_(N,L)` projects onto rows satisfying `floor(N/r)<=L` and `c_(Theta,delta)>0` is fixed. Every exact copy of every lower state `V_(a,D)` with `a<=L_H` and `a|N` is supported inside this same terminal sector. Hence even the **union of all exact small-anchor copies**, not merely one chosen common divisor, carries only `o(1)` of the normalized frontier state.

Consequently the additive thickness of `FD-084`, together with the exact dilation embedding of `FD-034`/`FD-067`, does not by itself solve the inter-block compatibility problem. Any successful common-multiple transport must obtain an anchor on a scale substantially larger than the block length, exploit a signed/bulk quantity outside the terminal quotient sector, or prove a destination-energy saving that changes the normalization.

## 1. Every integer dilation contains a uniformly conditioned exact Jordan copy

Retain the fixed-head physical Jordan vector from `FD-086`, zero-extended to the common space `ell^2({r>D})`:

\[
V_{H,D}(r)
:=
\sqrt{w(r)}\,
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right),
\qquad
w(r):=\frac{J_2(r)}{r^2},
\tag{3}
\]

so that

\[
\|V_{H,D}\|_2^2=E_{H,D}.
\tag{4}
\]

For an integer `q>=1`, define the row-dilation operator `mathscr D_q` by

\[
(\mathscr D_qx)(qr)
:=
\sqrt{\frac{w(qr)}{w(r)}}\,x(r)
\qquad(r>D),
\tag{5}
\]

and set it to zero on rows not of the form `qr` with `r>D`. Then the floor quotient gives the exact identity

\[
\boxed{
P_qV_{qH,D}=\mathscr D_qV_{H,D},
}
\tag{6}
\]

where `P_q` is the coordinate projection onto those dilated rows. Indeed,

\[
V_{qH,D}(qr)
=
\sqrt{w(qr)}\,
\mathcal H\!\left(\left\lfloor\frac{qH}{qr}\right\rfloor\right)
=
\sqrt{\frac{w(qr)}{w(r)}}V_{H,D}(r).
\tag{7}
\]

The Jordan weight has the Euler product

\[
w(n)=\prod_{p\mid n}(1-p^{-2}).
\tag{8}
\]

Therefore

\[
\frac{w(qr)}{w(r)}
=
\prod_{\substack{p\mid q\\p\nmid r}}(1-p^{-2}),
\tag{9}
\]

and every finite subproduct is bounded below by the full Euler product `1/zeta(2)`. Hence

\[
\boxed{
\frac1{\zeta(2)}\|x\|_2^2
\le
\|\mathscr D_qx\|_2^2
\le
\|x\|_2^2
}
\tag{10}
\]

for every `q`, with no dependence on its size or prime factorization. The inverse on the range of `mathscr D_q` has norm at most `sqrt(zeta(2))`.

This strengthens the bookkeeping viewpoint of `FD-034` and `FD-067`. Nonsquarefree `q` is needed there because the image rows must themselves witness nonsquarefree occupation. For **state transport**, no such restriction exists: every integer dilation contains a uniformly conditioned full copy.

There is also an exact common-multiple interpretation. If `a|N_1` and `a|N_2`, put

\[
M:=\operatorname{lcm}(N_1,N_2).
\tag{11}
\]

Both embedded states `mathscr D_(M/N_1)V_(N_1,D)` and `mathscr D_(M/N_2)V_(N_2,D)` are coordinate restrictions of `V_(M,D)`, and their common coordinate support contains

\[
\boxed{
\mathscr D_{M/a}V_{a,D}.
}
\tag{12}
\]

Thus a shared divisor is a genuine exact common Jordan anchor. There is no loss of raw information merely because the common multiple is large.

## 2. The whole low-source terminal sector has a sharp power bound

For a horizon `N` and source cutoff `1<=L<N`, let `Q_(N,L)` denote projection onto the rows for which

\[
\left\lfloor\frac Nr\right\rfloor\le L.
\tag{13}
\]

These are the large Jordan rows, beginning at `r>N/(L+1)`. By `FD-046`, for every fixed `sigma>Theta`,

\[
|\mathcal H(k)|\ll_\sigma k^\sigma.
\tag{14}
\]

Since `w(r)<=1`, (13)--(14) imply

\[
\begin{aligned}
\|Q_{N,L}V_{N,D}\|_2^2
&\le
\sum_{r>N/(L+1)}
\left|\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right)\right|^2\\
&\ll_\sigma
N^{2\sigma}
\sum_{r>N/(L+1)}r^{-2\sigma}.
\end{aligned}
\tag{15}
\]

Because `sigma>1/2`, the tail of the convergent `p`-series gives

\[
\boxed{
\|Q_{N,L}V_{N,D}\|_2^2
\ll_\sigma
N L^{2\sigma-1}.
}
\tag{16}
\]

This estimate uses the full row tail directly. In particular it has no additive `O(L^(2sigma+1))` floor-counting error, which would be too large in part of the false-RH range.

Equation (16) is the capacity bound relevant to common divisors. If `a|N` and `a<=L`, the exact copy `mathscr D_(N/a)V_(a,D)` is supported on rows `(N/a)r`. On every such row,

\[
\left\lfloor
\frac{N}{(N/a)r}
\right\rfloor
=
\left\lfloor\frac ar\right\rfloor
\le a\le L.
\tag{17}
\]

Therefore

\[
\boxed{
\operatorname{supp}(\mathscr D_{N/a}V_{a,D})
\subseteq
\operatorname{ran}Q_{N,L}.
}
\tag{18}
\]

The same inclusion holds simultaneously for **every** divisor `a<=L`; taking their union creates no new coordinates outside `Q_(N,L)`.

## 3. Near-frontier occupied blocks make that terminal sector negligible

The seed extraction in `FD-084`, equation (22) there, is stronger than the particular parameter choice later used to state its block theorem. For every fixed `kappa>0`, sufficiently late recurrent annuli contain an occupied seed `H` with

\[
E_{H,D}>H^{2\Theta-\kappa}.
\tag{19}
\]

Fix `0<delta<Theta`. Choose `kappa>0` sufficiently small compared with `delta`. Repeating the scalar transport step of `FD-084` with the local exponent losses chosen smaller than `delta-kappa` preserves constant occupation throughout

\[
I_H=[H,H+L_H],
\qquad
L_H:=\lfloor H^{\Theta-\delta}\rfloor.
\tag{20}
\]

Likewise, the vector displacement estimate of `FD-086` gives, uniformly for `N in I_H`,

\[
\frac{\|V_{N,D}-V_{H,D}\|_2^2}{E_{H,D}}
\ll
H^{-2\delta+\kappa}
+
H^{-\Theta-\delta+\gamma+\kappa}
=o(1)
\tag{21}
\]

for a sufficiently small fixed `gamma>0`. Consequently

\[
\boxed{
E_{N,D}=(1+o(1))E_{H,D}
>H^{2\Theta-\kappa}
}
\tag{22}
\]

uniformly on the whole block. Thus the near-frontier energy loss `kappa` can be chosen independently much smaller than the block-length loss `delta`; the earlier convenient choice `kappa=delta/2` is not load-bearing.

Now apply (16) with `L=L_H`, `N asymp H`, and `sigma=Theta+epsilon`. Equations (20) and (22) give

\[
\frac{\|Q_{N,L_H}V_{N,D}\|_2^2}{E_{N,D}}
\ll
H^{1+(\Theta-\delta)(2\Theta+2\varepsilon-1)-2\Theta+\kappa+o(1)}.
\tag{23}
\]

At `epsilon=kappa=0` the exponent is exactly

\[
1+(\Theta-\delta)(2\Theta-1)-2\Theta
=
-(2\Theta-1)(1-\Theta+\delta).
\tag{24}
\]

In the false-RH regime `Theta>1/2`, this is strictly negative; it remains so even if `Theta=1`, because then `delta>0`. Since both `epsilon>0` and `kappa>0` may be chosen arbitrarily small after `delta` is fixed, there is a constant `c_(Theta,delta)>0` for which

\[
\boxed{
\sup_{N\in I_H}
\frac{\|Q_{N,L_H}V_{N,D}\|_2^2}{E_{N,D}}
\ll H^{-c_{\Theta,\delta}}.
}
\tag{25}
\]

This proves (2). Notice the critical-line boundary: when `Theta=1/2`, the power margin in (24) disappears. The theorem is therefore genuinely false-RH-frontier-facing rather than a generic consequence of block thickness.

## 4. Exact common anchors supplied by additive thickness are asymptotically invisible

An interval of `L+1` consecutive integers contains a multiple of every integer `a<=L+1`. Hence if two occupied blocks have lengths at least `L`, additive thickness alone can always select one horizon in each block divisible by any prescribed common anchor `a<=L`.

Equations (12) and (10) show that this is an **exact**, uniformly conditioned raw-state bridge. But equations (18) and (25) show that, on a near-frontier block, every such bridge lands in a sector carrying only `o(1)` of the normalized physical state. In particular, uniformly over all divisors `a<=L_H` of any selected `N in I_H`,

\[
\boxed{
\frac{\|\mathscr D_{N/a}V_{a,D}\|_2^2}{E_{N,D}}
\le
\frac{\|Q_{N,L_H}V_{N,D}\|_2^2}{E_{N,D}}
=o(1).
}
\tag{26}
\]

More strongly, the union of the coordinate supports of **all** these exact anchor copies is still contained in the same `Q_(N,L_H)` sector, so summing over possible small anchors does not recover a constant share of the destination state by support coverage.

For two separated blocks, take any anchor no larger than the shorter block length and select a multiple of it in each block. At their least common multiple the two physical states really do contain the same embedded lower state, as (12) says. The obstruction is not entropy of the dilation factor and not poor conditioning of the embedding. It is normalization: the part of either frontier state that additive thickness can force into such a common anchor is asymptotically negligible.

This also explains why simply replacing the integer-ratio chain ruled out by `FD-085` with a gcd/lcm construction does not close the frontier left by `FD-086`. A bounded-norm multihorizon functional that sees only these guaranteed exact lower-horizon copies sees `o(1)` of each normalized block state.

## 5. Stress tests and scope boundary

The result does **not** say that two physical block horizons cannot accidentally have a common divisor much larger than their block lengths. Such an arithmetic coincidence could place a larger exact copy outside the terminal sector controlled here. The statement is about what additive thickness itself guarantees without a new compatibility theorem. Any future result forcing common divisors `a>>L_H` would evade this obstruction and would be genuinely new input.

Likewise, (25) does not say that the whole terminal sector is unimportant for unnormalized identities. Its absolute energy can grow. The conclusion is projective: relative to the near-frontier energy `E_(N,D)`, that sector vanishes. An `H`-dependent operator that amplifies it by an unbounded factor can of course produce a nonzero output, but then the amplification/conditioning cost must be included; (10) shows that the canonical dilation map itself does not supply such amplification.

The proof is fixed-head, as are `FD-084` and `FD-086`. Growing `D` changes both the near-frontier block theorem and the terminal-sector denominator and is not covered. The source envelope (14) is also essential. A generic bounded-increment synthetic profile need not satisfy the same zero-frontier power law, so this obstruction is more arithmetic than the transport inequality of `FD-086` alone.

Finally, no pointwise Schur gap or RH implication follows from (25). The theorem removes a natural inter-block composition mechanism: **small exact dilation anchors, even taken collectively, cannot carry constant normalized Jordan mass across the frontier blocks already available.** The live alternatives are a genuinely larger divisor/floor-quotient compatibility, a signed bulk functional that composes without restricting to the low-source terminal sector, or a same-horizon denominator saving.

## 6. Prior-art boundary

The literature audit covered the existing Farey/Mertens, Smith/GCD-matrix, and floor-quotient sources already anchored in `SOURCES.md`, together with targeted searches for dilation/least-common-multiple transport of Jordan-totient weighted floor-quotient states. The floor-quotient partial-order literature of Lagarias--Richman studies the order structure generated by `floor(n/k)`, while the classical Smith-matrix literature supplies the divisor-incidence factorization behind the Jordan coordinates. No located source states the vector dilation isomorphism (6)--(10) for this physical Farey--Mertens state, nor the false-RH terminal-sector capacity estimate (25), nor their consequence for additive-block common-anchor transport. This absence is not treated as a priority claim.

No new external theorem is load-bearing. The proof uses the exact Mathia Jordan representation, the zero-frontier source envelope of `FD-046`, and the recurrent near-frontier block/transport results `FD-084` and `FD-086`; the remaining inputs are the Euler product for `J_2(n)/n^2`, a convergent `p`-series tail, and elementary divisibility. Accordingly `SOURCES.md` requires no update.