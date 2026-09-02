# WI-100 — Near-saturated prime rotation resonances have bounded boundary width and incidence

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + STRUCTURAL-CLASSIFICATION`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It sharpens WI-091, WI-094, and WI-099 on the residual prime Ramanujan sector. WI-099 shows that every nonzero pairwise rank defect is phase-pure: all free cycles have one common reduced rotation type `m/ell`. The new point is that this already forces an exact two-sided capacity constraint on the boundary remainder. If the cycle packing is within bounded slack of saturation, the allowed boundary has bounded width, and at fixed observation length the corresponding prime-pair graph has bounded degree for **every** low-denominator resonance, not only the special one-third layer of WI-091. Combined with WI-094, every fixed-slack extensive-defect resonance sector contributes only `O(P^{-1})` of the dyadic Hilbert--Schmidt energy.

Let `p<q<2p` be distinct odd primes and work in the genuinely residual exceptional strip of WI-088/WI-096/WI-099,

\[
 d=q-p,
 \qquad
 t=p-d=2p-q,
 \qquad
 \delta=kq+s,
 \qquad
 d<s<p.
 \tag{1}
\]

The partial map has domain

\[
 A=\{0,\ldots,s-d-1\},
 \qquad
 B=\{s,\ldots,p-1\},
 \tag{2}
\]

so

\[
 |A|=s-d,
 \qquad
 |B|=p-s,
 \qquad
 |A|+|B|=t.
 \tag{3}
\]

Assume the residual row-rank defect is nonzero. WI-099 then gives integers `ell>=3`, `m>=1`, `a in {1,...,ell-1}`, and `c>=2` such that every free cycle has exactly `ell` vertices, every cycle has exactly `a` vertices in `A` and `ell-a` vertices in `B`,

\[
 \gcd(m,\ell)=1,
 \qquad
 k=\left\lfloor\frac{mp}{\ell}\right\rfloor,
 \qquad
 a=mp-\ell k,
 \tag{4}
\]

and

\[
 \tau_{p,q}=c-1.
 \tag{5}
\]

The union `F` of the free cycles has size `c ell` and lies inside `A union B`.

## 1. Phase purity gives an exact capacity tent

Because every free cycle uses exactly `a` vertices of `A` and `ell-a` vertices of `B`, disjointness gives the two capacity inequalities

\[
 \boxed{
 ca\le s-d,
 \qquad
 c(\ell-a)\le p-s.
 }
 \tag{6}
\]

Equivalently,

\[
 \boxed{
 \tau_{p,q}
 \le
 \min\left\{
 \left\lfloor\frac{s-d}{a}\right\rfloor,
 \left\lfloor\frac{p-s}{\ell-a}\right\rfloor
 \right\}-1.
 }
 \tag{7}
\]

Thus every reduced rotation type `(m,ell)` has a two-sided piecewise-linear **capacity tent** in the boundary remainder `s`. This is an upper envelope, not an assertion that every point under the tent is attained. WI-091 proves an exact attained triangle for the special `ell=3` opposite-residue layer; equation (7) is the general structural statement available from phase purity alone.

Define the unused capacities

\[
 u_A:=(s-d)-ca,
 \qquad
 u_B:=(p-s)-c(\ell-a).
 \tag{8}
\]

They are nonnegative integers. Their sum is exactly

\[
 \boxed{
 U:=u_A+u_B
 =t-c\ell
 =t-(\tau_{p,q}+1)\ell.
 }
 \tag{9}
\]

The quantity `U` is the number of domain vertices not belonging to free cycles. It is therefore an exact packing-slack variable, not an auxiliary estimate.

For fixed `c,ell,a`, (6) is the exact interval

\[
 \boxed{
 d+ca\le s\le p-c(\ell-a),
 }
 \tag{10}
\]

and the width of that interval is exactly

\[
 \boxed{U.}
 \tag{11}
\]

So once the common rotation type and the number of free cycles are fixed, every possible boundary remainder is confined to an interval whose width equals the number of nonrecurrent domain vertices.

## 2. Near-saturation forces a second rational phase

The natural center of the capacity tent is

\[
 s_*:=d+\frac{a}{\ell}t.
 \tag{12}
\]

Using `s=d+ca+u_A` and `t=c ell+U`, one gets the exact identity

\[
 \boxed{
 s-s_*=u_A-\frac{a}{\ell}U.
 }
 \tag{13}
\]

Hence

\[
 \boxed{
 -\frac{a}{\ell}U
 \le s-s_*
 \le \frac{\ell-a}{\ell}U.
 }
 \tag{14}
\]

If

\[
 \rho:=\frac{c\ell}{t}=1-\frac Ut,
 \tag{15}
\]

then, after division by `t`,

\[
 \boxed{
 -\frac a\ell(1-\rho)
 \le
 \frac{s-d}{t}-\frac a\ell
 \le
 \frac{\ell-a}{\ell}(1-\rho).
 }
 \tag{16}
\]

WI-095/WI-099 already force the quotient `k/p` toward the reduced rotation `m/ell` when the defect is extensive. Equation (16) gives a complementary phase locking: near saturation of the recurrent capacity forces the **boundary-position ratio** `(s-d)/t` toward the rational `a/ell`.

There is a particularly clean additive formulation. Put

\[
 h:=\left\lfloor\frac t\ell\right\rfloor.
 \tag{17}
\]

If the cycle count is within `D` of the largest count allowed by total capacity,

\[
 c\ge h-D,
 \tag{18}
\]

then

\[
 \boxed{
 U=t-c\ell
 \le (t\bmod\ell)+D\ell
 \le \ell(D+1)-1.
 }
 \tag{19}
\]

Equivalently, if the defect `tau=c-1` is within additive `D` of the crude layer ceiling `h-1`, the boundary interval has width at most `ell(D+1)-1`. At exact full packing `U=0`, necessarily `ell|t` and the boundary remainder is unique:

\[
 \boxed{
 s=d+\frac a\ell t.
 }
 \tag{20}
\]

This is the all-denominator analogue of the localization mechanism behind WI-091's exact one-third boundary, without claiming WI-091's exact rank formula outside `ell=3`.

## 3. Fixed observation length turns bounded slack into bounded incidence

The preceding interval can be converted into a congruence that controls how many other primes can share the same near-saturated resonance at a fixed observation length.

Define the integer boundary error

\[
 E:=\ell(s-d)-at.
 \tag{21}
\]

By (13), or directly from (8)--(9),

\[
 E=\ell u_A-aU,
 \tag{22}
\]

so

\[
 \boxed{
 -aU\le E\le(\ell-a)U.
 }
 \tag{23}
\]

Since `d=q-p` and `t=2p-q`, equation (21) gives

\[
 \ell s
 = (\ell-a)q+(2a-\ell)p+E.
 \tag{24}
\]

Using `delta=kq+s` and the WI-099 identity `ell k+a=mp`,

\[
 \boxed{
 \ell\delta
 =(mp+\ell-2a)q+(2a-\ell)p+E.
 }
 \tag{25}
\]

Therefore

\[
 \boxed{
 \ell\delta\equiv(\ell-2a)q+E\pmod p,
 }
 \tag{26}
\]

and symmetrically

\[
 \boxed{
 \ell\delta\equiv-(\ell-2a)p+E\pmod q.
 }
 \tag{27}
\]

The coefficient `ell-2a` never vanishes. Indeed, WI-099 gives `gcd(m,ell)=1` and `a congruent mp (mod ell)`; since `ell<p` and `p` is prime, `gcd(a,ell)=1`. Equality `ell=2a` would therefore force `ell=2`, contradicting `ell>=3`. Also `|ell-2a|<ell<p<q`, so the coefficient is nonzero modulo both primes.

At a fixed observation length `N`, the nearest-`pq` boundary convention gives a sign `eta in {+1,-1}` such that

\[
 N\equiv\eta\delta\pmod{pq}.
 \tag{28}
\]

Thus

\[
 \boxed{
 \ell N
 \equiv
 \eta\big((\ell-2a)q+E\big)
 \pmod p,
 }
 \tag{29}
\]

and

\[
 \boxed{
 \ell N
 \equiv
 \eta\big(- (\ell-2a)p+E\big)
 \pmod q.
 }
 \tag{30}
\]

Fix a reduced resonance `m/ell` and a slack ceiling `U<=U_0`. For a fixed smaller endpoint `p`, equations (4) determine `a`, and (23) gives at most

\[
 \ell U_0+1
 \tag{31}
\]

possible integer values of `E`. For each pair `(eta,E)`, (29) determines at most one residue class for `q modulo p`; the close-prime interval `p<q<2p` contains at most one integer from that class. Hence the number of edges for which `p` is the smaller endpoint is at most

\[
 \boxed{2(\ell U_0+1).}
 \tag{32}
\]

For a fixed larger endpoint `q`, the smaller prime `p` may give different `a`, but (4) and `gcd(m,ell)=1` imply that `a` is a reduced residue modulo `ell`. There are at most `phi(ell)` possibilities. For each `(a,eta,E)`, (30) determines at most one `p modulo q`, and `0<p<q` contains at most one representative. Thus the number of edges for which `q` is the larger endpoint is at most

\[
 \boxed{2\varphi(\ell)(\ell U_0+1).}
 \tag{33}
\]

Consequently the undirected fixed-`N` graph of one reduced resonance layer satisfies

\[
 \boxed{
 \Delta_{m/\ell,U_0}
 \le
 2(1+\varphi(\ell))(\ell U_0+1).
 }
 \tag{34}
\]

For the additive near-saturation condition (18), one may take

\[
 U_0=\ell(D+1)-1,
 \tag{35}
\]

so `Delta=O_ell(D+1)`, uniformly in `N`, `p`, and the dyadic prime scale.

This genuinely extends WI-091's bounded-incidence principle. WI-091 gets a sharper constant `8D+4` by exploiting the exact `ell=3` triangular profile. Equation (34) is weaker there, but it applies to every phase-pure resonance denominator supplied by WI-099.

## 4. All near-saturated extensive layers are cumulatively `O(P^{-1})`

WI-099 proves that a `theta`-extensive residual defect,

\[
 \tau_{p,q}\ge\theta p,
 \tag{36}
\]

forces

\[
 \ell<\frac1\theta.
 \tag{37}
\]

Thus, for fixed `theta`, there are only finitely many possible reduced resonances `m/ell` with `ell>=3` and `0<m/ell<1/2`. Summing (34) over those finitely many layers shows that the union of all `theta`-extensive edges with a common slack ceiling `U<=U_0` has

\[
 \boxed{
 \Delta_{\theta,U_0}=O_{\theta,U_0}(1).
 }
 \tag{38}
\]

More explicitly, one may take the finite constant

\[
 \Delta_{\theta,U_0}
 \le
 \sum_{\substack{3\le\ell<1/\theta\\1\le m<\ell/2\\(m,\ell)=1}}
 2(1+\varphi(\ell))(\ell U_0+1).
 \tag{39}
\]

Now apply WI-094. Every `theta`-extensive pair in a dyadic scale `[P,2P]` has normalized Frobenius coherence less than

\[
 \frac{4}{\theta(P-1)}.
 \tag{40}
\]

WI-094's Hilbert-space aggregation uses only this edgewise coherence and a maximum-degree bound. Replacing its trivial degree `M-1` by (38), for arbitrary real source weights one obtains

\[
 \boxed{
 |\mathcal C_{\theta,U_0}|
 \le
 \frac{4\Delta_{\theta,U_0}}{\theta(P-1)}\,\mathcal D
 =O_{\theta,U_0}(P^{-1})\mathcal D.
 }
 \tag{41}
\]

Here `mathcal D` is WI-094's diagonal Frobenius energy and `mathcal C_{theta,U_0}` is the cross term restricted to extensive residual edges whose recurrent packing slack is at most `U_0`.

This improves WI-094's general `O_theta(1/log P)` cumulative bound by a full prime-counting factor on the near-saturated sector. In particular, **no bounded-slack low-denominator resonance layer can become a macroscopic cancellation resource by proliferating across many comparable primes**. The special one-third statement in WI-094 §5 is now one instance of a general phase-pure resonance mechanism.

The same counting also gives a graded version. If a family has a scale-dependent common slack bound `U_0(P)`, then the finite sum in (39) is `O_theta(U_0(P)+1)`, hence

\[
 \boxed{
 |\mathcal C_{\theta,U_0(P)}|
 =O_\theta\left(\frac{U_0(P)+1}{P}\right)\mathcal D.
 }
 \tag{42}
\]

So every extensive-defect sector with `U=o(P)` is cumulatively negligible even before invoking prime sparsity. WI-094 remains necessary for the unrestricted case because `U` may itself be of order `P`.

## 5. Stress tests, prior-art boundary, and what is not proved

The exact derivation is falsified by any WI-099 residual pair for which a free cycle uses a different `A/B` population, by any violation of (6), or by any fixed-`N` pair violating congruences (29)--(30). An exact finite enumeration of residual close-prime parameters for primes below `80` produced `5,147` instances with at least two free cycles and found no violation of the WI-099 phase-purity data, the capacity inequalities, the width identity (9)--(11), or the boundary-error congruence. Those computations are **falsification only** and are not evidence for the theorem; equations (6)--(42) are exact consequences of the persisted WI-099/WI-094 theorems.

The prior-art audit rechecked the two surrounding literatures already anchored for this sector. Classical Ramanujan-subspace work, including P. P. Vaidyanathan's 2014 IEEE papers and the exact-period spectral identities recorded in `SOURCES.md`, supplies the harmonic-analysis setting but not the finite-window close-prime resonance counting used here. Classical rotation/period-adding theory, including the Granados--Alsedà--Krupa survey cited in WI-099, supplies the general language of rational rotation layers and mode locking. No source located in that audit formulates the exact capacity identities (6)--(14), the prime congruences (29)--(30), or the resulting fixed-observation incidence bound (34) for Ramanujan cross Grams. **No priority claim is made.**

Several stronger statements suggested by finite experiments are deliberately **not** promoted. For denominators `ell>3`, many small examples appear to have an exactly attained triangular cycle-count profile as `s` moves through the resonance layer, analogous to WI-091. The present proof establishes only the universal capacity tent and its stability consequences; it does not prove exact attainment or an exact rank formula for general `ell`. Nor does it show that the packing slack `U` is bounded or sublinear for all extensive defects. Therefore it does not supersede WI-094's unrestricted `O_theta(1/log P)` theorem and does not close the full scalar Yang welding problem.

## 6. Program consequence

WI-099 left open a collective escape: even though one pair is forced onto one rational rotation, many different prime pairs might occupy the same layer and accumulate. The capacity identities show that this escape requires **macroscopic nonrecurrent slack** if it is to evade bounded incidence. Whenever the free cycles nearly fill the available residual domain, the boundary is locked to a narrow rational tent, fixed-`N` congruences make the prime graph sparse, and WI-094 turns that sparsity into `O(P^{-1})` cumulative coherence.

The residual rank-defect program is therefore narrowed one step further. A source-faithful cancellation mechanism cannot be built from a dense cloud of near-saturated low-denominator rank defects. Any remaining pairwise extensive-defect contribution capable of saturating WI-094's weaker `O(1/log P)` scale must live in layers with substantial packing slack `U`, while a fixed-fraction Yang cancellation must still come from the low-/zero-defect regime, cross-scale structure, the exact signed coefficient law, or information discarded by scalarization. The next useful structural question is consequently whether arithmetic or finite-window dynamics can force `U=o(p)` (or conversely construct `U asymp p`) on every extensive phase-pure resonance.