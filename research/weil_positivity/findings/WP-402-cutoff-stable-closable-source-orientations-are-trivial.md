---
id: WP-402
title: Cutoff-stable closable source orientations are trivial
branch: weil_positivity
status: supported
kind: cstar-hereditary-source-fixed-shadow-closable-operator-pointed-cone-orientation-obstruction
claim_strength: exact RH-independent extension of WP-401 from bounded scalar sign readouts to possibly unbounded closable Banach-valued linear orientation maps on any hereditary source domain stable under the canonical continuous cutoffs; every such map vanishes, so any nonzero linear escape of this type is necessarily nonclosable or cutoff-unstable
created: 2026-09-22
related: [WP-394, WP-399, WP-400, WP-401]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - T. Kato, Perturbation Theory for Linear Operators, 2nd ed., Springer, Chapter III section 5, closed and closable operators
  - B. Blackadar, Operator Algebras: Theory of C*-Algebras and von Neumann Algebras, Springer (2006), hereditary C*-subalgebras and approximate units
  - J. Tomiyama, On the projection of norm one in W*-algebras, Proc. Japan Acad. 33 (1957), 608--612, DOI 10.3792/pja/1195524885
---

# WP-402 — Cutoff-stable closable source orientations are trivial

## Claim

`WP-401` proves that continuous source cutoffs make two-sided positive tangents norm dense in a hereditary fixed-shadow fibre. Its final scalar conclusion uses boundedness of the readout to pass from the cutoff approximants back to the original direction, and therefore leaves an explicit apparent escape: replace the bounded scalar functional by a genuinely unbounded linear boundary response.

Closability already closes that escape, even for operator-valued responses.

Let `A` be a C-star algebra, `B subseteq A` a C-star subalgebra, and

\[
E:A\to B
\]

be a conditional expectation. Fix `d in B_+`, put

\[
H_d=\operatorname{Her}_A(d)=\overline{dAd},
\qquad
V_d=\{k\in(H_d)_{\rm sa}:E(k)=0\},
\tag{1}
\]

and use the canonical continuous cutoffs from `WP-401`,

\[
f_n(t)=\min(1,nt),
\qquad
c_n=f_n(d).
\tag{2}
\]

Let `D subseteq V_d` be a real linear space satisfying

\[
k\in D\quad\Longrightarrow\quad c_nkc_n\in D
\qquad(n\ge1).
\tag{3}
\]

Let `Y` be a real Banach space with a pointed cone `C`, so

\[
C\cap(-C)=\{0\},
\tag{4}
\]

and let

\[
T:D\to Y
\tag{5}
\]

be a linear operator that is closable for the C-star norm on `D subset H_d` and the norm topology of `Y`. Assume positivity of the fixed-shadow fibre is supposed to orient the response in the sense that

\[
d+h\ge0,\ h\in D
\quad\Longrightarrow\quad
T(h)\in C.
\tag{6}
\]

Then

\[
\boxed{T=0\text{ on }D.}
\tag{7}
\]

Equivalently, **every nonzero linear source orientation satisfying (3) and (6) is nonclosable**. Thus moving from bounded scalar readouts to an unbounded but closable operator-valued boundary response does not evade the hereditary source-local sign obstruction. A surviving linear mechanism must fail the canonical cutoff stability, fail closability, or leave this fixed-shadow hereditary category.

This is not a statement that all unbounded source operators vanish. Cutoff-stable unbounded closed operators exist abundantly. What is incompatible with closability is the additional demand that ordinary positivity of `d+h` place the entire linear response into one pointed target cone.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CSTAR-HEREDITARY-SOURCE-CORNER + CONDITIONAL-EXPECTATION + CONTINUOUS-CUTOFF-STABILITY + POSSIBLY-UNBOUNDED-LINEAR-READOUT + BANACH-VALUED + POINTED-CONE-ORIENTATION + CLOSABILITY-GRAPH-GATE + EXPLICIT-NONCLOSABILITY-WITNESS + SOURCE-LOCALITY-OBSTRUCTION + MATCHED-CONTROL-UNIVERSAL + NOT-A-WEIL-BRIDGE`.

## 1. Cutoff localization kills every localized response exactly

Fix `k in D` and define

\[
k_n=c_nkc_n.
\tag{8}
\]

By (3), every `k_n` lies in `D`. The `WP-401` cutoff calculation is internal to the present hypotheses and gives

\[
k_n\longrightarrow k\quad\text{in C-star norm}
\tag{9}
\]

and

\[
-n\|k\|d\le k_n\le n\|k\|d.
\tag{10}
\]

For `k !=0`, choose any

\[
0<\varepsilon_n\le (n\|k\|)^{-1}.
\tag{11}
\]

Then (10) gives both

\[
d+\varepsilon_n k_n\ge0,
\qquad
d-\varepsilon_n k_n\ge0.
\tag{12}
\]

Because `D` is linear, both `+epsilon_n k_n` and `-epsilon_n k_n` are in its domain. Applying the orientation rule (6) to the two signs yields

\[
\varepsilon_nT(k_n)\in C,
\qquad
-\varepsilon_nT(k_n)\in C.
\tag{13}
\]

Since `epsilon_n>0` and `C` is pointed,

\[
T(k_n)=0
\qquad\text{for every }n.
\tag{14}
\]

For `k=0` the same conclusion is trivial. Therefore the positivity geometry does more than make the localized responses small: it annihilates each one exactly.

## 2. Closability turns the cutoff tail into an explicit graph obstruction

The remaining step does not require boundedness or continuity of `T`. Set

\[
r_n=k-k_n.
\tag{15}
\]

Linearity of `D`, (3), and (9) imply

\[
r_n\in D,
\qquad
r_n\longrightarrow0
\quad\text{in C-star norm}.
\tag{16}
\]

But by (14),

\[
T(r_n)=T(k)-T(k_n)=T(k)
\qquad\text{for every }n.
\tag{17}
\]

Hence `T(r_n)` converges in `Y`, and its limit is exactly `T(k)`. The standard graph criterion for closability says that whenever domain vectors converge to zero and their images converge, the image limit must be zero. Therefore

\[
T(k)=0.
\tag{18}
\]

Since `k in D` was arbitrary, (7) follows.

The contrapositive is sharper than a mere failure of continuity. If a nonzero `T` satisfies the positivity-orientation rule and the cutoff invariance, choose `k` with `T(k) !=0`. Then the explicit sequence

\[
r_n=k-c_nkc_n
\tag{19}
\]

satisfies

\[
r_n\to0,
\qquad
T(r_n)\to T(k)\ne0.
\tag{20}
\]

Thus the canonical hereditary cutoffs themselves exhibit the vertical vector `(0,T(k))` in the closure of the graph. The obstruction is therefore exactly nonclosability, not merely the absence of a convenient boundedness estimate.

## 3. This genuinely extends the bounded scalar conclusion

`WP-401` ends with a bounded real linear functional `L`. There, after proving `L(k_n)=0`, norm continuity gives `L(k)=0`. The present result replaces that final continuity step by the graph criterion and allows `T` to take values in an infinite-dimensional Banach space. This matters because unbounded closed or closable Banach-valued operators are a genuine class rather than a terminological reformulation of bounded functionals.

A simple matched control makes the distinction concrete. Let

\[
A=C_0((0,1])\oplus C_0((0,1]),
\]

let `B` be the diagonal copy of `C_0((0,1])`, and let `E` average the two coordinates. With

\[
d(x)=(x,x),
\]

`d` is strictly positive and `H_d=A`, while

\[
V_d=\{(h,-h):h\in C_0((0,1])_{\rm sa}\}.
\tag{21}
\]

On the cutoff-stable domain

\[
D=\{(h,-h):x^{-1/2}h(x)\in L^2(0,1)\},
\]

the multiplication operator

\[
T(h,-h)=x^{-1/2}h(x)
\tag{22}
\]

is closed from the C-star sup norm domain into `L^2(0,1)` and is unbounded: continuous functions of sup norm one that switch from zero near `0` to one on `[e^{-m},1]` have image norm of order `sqrt(m)`. Multiplication by the bounded cutoffs `c_n(x)=min(1,nx)` preserves `D`.

This operator of course does **not** satisfy (6), as the theorem predicts. Its role is only to show that the class “unbounded, closable, cutoff-stable linear operator” is nonempty and natural. The no-go comes from combining that class with a one-sided cone orientation forced solely by positivity of the fixed-shadow fibre.

## 4. Relation to the earlier unbounded-form obstruction

`WP-394` also studies an unbounded category, but the mechanism and hypotheses are different. There a nonnegative closed quadratic form `q` with self-adjoint operator `S>=0` is assumed to have one canonical resolvent `(S+lambda I)^{-1}` inside the represented bounded Bost--Connes source algebra. Exact mixed-prime nullity then passes through the bounded transform `S(S+lambda I)^{-1}` and collapses by `WP-392`.

Here no resolvent of `T` is assumed to lie in the source algebra, and `T` need not be self-adjoint, positive, Hilbert-space valued, or even an operator on the source Hilbert space. Instead, the input is a **linear ordered response** on source perturbations. The conclusion comes from two-sided positive cutoff tangents plus closability of its graph.

Conversely, the present theorem does not rule out positive closed quadratic forms merely because they are closable. A form such as

\[
q(h)=\|Th\|^2
\]

is even in `h` and does not satisfy the oriented linear rule (6). Nor does the theorem say that a positive self-adjoint unbounded selector with a source-external resolvent is impossible. The two obstructions close different escape routes and should not be conflated.

## 5. Relevance to the Bost--Connes completion fork

The accepted Bost--Connes clue asks for a source-forced global completion whose positivity has enough orientation to survive the finite-place and archimedean assembly. `WP-395`--`WP-401` progressively show that centralizer shadows, modular-frequency packaging, quotients, and source-local fixed-shadow linear relations do not obtain such an orientation for free.

After `WP-401`, one could still try to put the missing sign into an unbounded linear boundary map and argue that bounded duality was the only obstruction. The theorem above rules out exactly that move whenever the map remains closable and its source domain respects the canonical continuous localizations generated by the fixed shadow `d`.

The mathematical fork is consequently narrower. A nontrivial linear source response must now exhibit at least one substantive nonlocal feature: its domain is not preserved by `k -> f_n(d)kf_n(d)`, its graph is deliberately singular/nonclosable, or its sign is not an ordinary pointed-cone consequence of `d+h>=0`. Alternatively, the mechanism must become nonlinear/quadratic, one-sided, representation-changing, or genuinely global through a finite--archimedean coupling.

Because the proof uses no prime arithmetic, it is again a matched-control obstruction. The same theorem holds in any C-star algebra with the stated hereditary fixed-shadow structure. Therefore this geometry alone cannot explain why the Riemann finite-place data should acquire the particular global Weil orientation.

## 6. Prior-art and novelty audit

All functional-analytic ingredients are classical. Kato's treatment of closed and closable operators gives the graph criterion used in (16)--(18). Hereditary C-star subalgebras and continuous approximate units are standard operator-algebra theory, with Blackadar providing a convenient reference, and conditional-expectation bimodularity is classical in the line of Tomiyama.

A bounded literature search combining hereditary C-star subalgebras, conditional expectations, closable operators, ordered Banach targets, and the Bost--Connes system found those standard ingredients and nearby structural results, but no direct theorem asserting this fixed-shadow arithmetic-source consequence. No external novelty is claimed for the abstract graph argument. The line-specific research delta is the exact synthesis with `WP-401`: the canonical cutoff tail is an explicit graph-defect sequence for every attempted nonzero closable orientation.

That distinction is important for evidence classification. `WP-402` is an **exact derived obstruction**, not a claim that a new general theorem of operator theory has been discovered. Its relevance comes from closing a declared escape route in the Mathia source-completion search while preserving a precise category boundary.

## 7. Boundaries and decisive audit test

The pointedness assumption is essential to the stated conclusion. If the target cone has nontrivial lineality `C intersect (-C)`, the two-sign argument only places each localized response in that lineality. A genuine orientation should therefore be tested after quotienting out any such neutral directions.

Cutoff stability is equally essential. If the arithmetic domain `D` is destroyed by `c_nkc_n`, the sequence (19) is unavailable. Such failure is now a concrete thing a proposed cross-scale source relation can demonstrate rather than a generic appeal to unboundedness. The theorem also does not cover nonlinear maps, merely one-sided admissible domains, quadratic energies, or a finite--archimedean assembly in which the source direction itself changes under completion.

The decisive audit is exact and local: produce a nonzero `k in D` satisfying all stated hypotheses. Equations (8)--(14) force every cutoff image to zero under `T`, and (19)--(20) then either force `T(k)=0` or explicitly violate closability. There is no asymptotic estimate, regularization convention, RH assumption, zero coding, or numerical tolerance on which the conclusion depends.

Accordingly this finding does not supply Weil positivity. It removes one more source-local way of pretending that positivity has acquired orientation: **unboundedness without nonclosability or cutoff-breaking structure is not an escape.**