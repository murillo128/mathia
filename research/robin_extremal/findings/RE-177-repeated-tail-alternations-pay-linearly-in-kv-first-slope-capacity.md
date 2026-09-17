# RE-177 — Repeated tail alternations pay linearly in KV first-slope capacity

**Status:** `EXACT-DERIVED + PRIME-SUPPORTED + TWO-JET-MATCHING + FINITE-SIGN-COMPLEXITY + KV-TAIL-CAPACITY + OSCILLATION-TARIFF + ROBIN-SCALE-CONDITIONING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-169, RE-173, RE-175, RE-176.

`RE-176` prices the minimal `- + -` repair of the `RE-173` transient Robin excursion: once the Mertens charge and first Euler boundary slope are both matched, a terminal one-sign tail beginning at `Y` cannot be pushed beyond the first-slope KV capacity horizon.

The surviving escape was to keep alternating signs after `Y`, so that the cumulative Chebyshev discrepancy could cancel internally and terminal monotonicity would disappear. The main point here is that **finitely many later alternations buy only linearly more weighted tail capacity**.

Retain the canonical `RE-173` deletion packet

\[
D_p\subset[2p,3p],
\qquad
c_q=-1\quad(q\in D_p),
\tag{1}
\]

with Mertens mass

\[
d_p:=\sum_{q\in D_p}H(q)
\asymp \frac1{\sqrt p\log p},
\qquad
H(q):=\log\frac q{q-1}.
\tag{2}
\]

Let the first positive phase `P` be supported in `[lambda p,Y)`, where `lambda>3` is fixed and `c_q>0` on its nonzero coefficients. After `Y`, allow arbitrary integer multiplicities and arbitrary spacing, but suppose the nonzero tail coefficients form only `M` maximal sign-constant phases. Assume exact two-jet matching

\[
D_Q(1+)=D_Q'(1+)=0
\tag{3}
\]

and the same matched-source KV fidelity as before,

\[
|\Delta\vartheta(x)|
:=|\vartheta_Q(x)-\vartheta(x)|
\le C_b x e^{-bV(x)},
\qquad
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}.
\tag{4}
\]

Then, with

\[
\ell_{\rm KV}(Y):=\frac{\log Y}{V(Y)},
\tag{5}
\]

one necessarily has

\[
\boxed{
\sqrt p\log p\,
\bigl(M+\ell_{\rm KV}(Y)\bigr)e^{-bV(Y)}
\gg_{b,\lambda}1.
}
\tag{6}
\]

Thus `RE-176` was not merely a one-sign accident. A subpolynomial number of later sign phases cannot move the leading KV horizon at all:

\[
M=p^{o(1)}
\quad\Longrightarrow\quad
\boxed{
bV(Y)\le\left(\frac12+o(1)\right)\log p.}
\tag{7}
\]

More sharply, if a repair is delayed to

\[
bV(Y)\ge\left(\frac12+\delta\right)\log p
\tag{8}
\]

for fixed `delta>0`, then

\[
\boxed{
M\ge p^{\delta-o(1)}.
}
\tag{9}
\]

Repeated cancellation therefore trades **KV distance for sign-phase complexity**. Crossing a fixed positive fraction beyond the `1/2` first-slope horizon requires polynomially many later alternations; merely adding finitely, polylogarithmically, or more generally subpolynomially many phases does not suffice.

## 1. Two exact boundary coordinates leave a centered slope debt

Use the `RE-175` notation

\[
B(q):=-J_1(q)=\frac{\log q}{q-1},
\qquad
A(q):=\frac{B(q)}{H(q)}.
\tag{10}
\]

The elementary bounds there give

\[
\log q<A(q)<\frac q{q-1}\log q.
\tag{11}
\]

For the deletion phase put

\[
h_D:=\sum_{q\in D_p}H(q)=d_p,
\qquad
b_D:=\sum_{q\in D_p}B(q),
\qquad
a_D:=\frac{b_D}{h_D}.
\tag{12}
\]

For the first positive phase put

\[
h_P:=\sum_{q\in P}c_qH(q),
\qquad
b_P:=\sum_{q\in P}c_qB(q),
\qquad
a_P:=\frac{b_P}{h_P}.
\tag{13}
\]

Let `T` denote the complete signed tail supported on primes `q>=Y`, and write

\[
h_T:=\sum_{q\ge Y}c_qH(q),
\qquad
b_T:=\sum_{q\ge Y}c_qB(q).
\tag{14}
\]

Exact Mertens and first-slope matching are

\[
-h_D+h_P+h_T=0,
\qquad
-b_D+b_P+b_T=0.
\tag{15}
\]

Eliminate `h_P,b_P` by centering at the actual positive-phase barycenter `a_P`. Equations (13)--(15) give the exact identity

\[
\begin{aligned}
b_T-a_Ph_T
&=(b_D-b_P)-a_P(h_D-h_P)\\
&=b_D-a_Ph_D\\
&=h_D(a_D-a_P).
\end{aligned}
\tag{16}
\]

This is the key observation. It does **not** require the future tail to have one sign, nor does it depend on how much Mertens mass the first positive phase carries. The entire later repair must transport the centered kernel

\[
K_P(q):=B(q)-a_PH(q)
\tag{17}
\]

with signed total

\[
\boxed{
\left|\sum_{q\ge Y}c_qK_P(q)\right|
=h_D(a_P-a_D).
}
\tag{18}
\]

Because `D_p subset [2p,3p]` and `P subset [lambda p,Y)`, (11) yields

\[
a_D\le(1+o(1))\log(3p),
\qquad
a_P\ge\log(\lambda p).
\tag{19}
\]

Hence

\[
\boxed{
\left|\sum_{q\ge Y}c_qK_P(q)\right|
\ge
\bigl(\log(\lambda/3)-o(1)\bigr)d_p.
}
\tag{20}
\]

So the fixed Robin-scale workload found in `RE-176` survives even when the remote tail is allowed to oscillate. What changes is only how much absolute weighted mass the KV envelope can hide by repeated resets of the cumulative discrepancy.

## 2. Finite sign complexity bounds total weighted tail variation

We isolate the generic capacity lemma used below.

Let a signed prime tail start at `Y`, and suppose its nonzero coefficients split into `M` maximal sign-constant phases. Let the starting points be

\[
Y=y_1<y_2<\cdots<y_M,
\tag{21}
\]

with the last phase possibly infinite. Assume throughout the tail that

\[
|\Delta\vartheta(x)|\le E_b(x),
\qquad
E_b(x):=C_bxe^{-bV(x)}.
\tag{22}
\]

Inside phase `j`, define its increasing absolute Chebyshev mass

\[
M_j(x)
:=
\sum_{\substack{y_j\le q\le x\\q\text{ in phase }j}}
|c_q|\log q.
\tag{23}
\]

Since the sign is constant within the phase,

\[
M_j(x)
=
|\Delta\vartheta(x)-\Delta\vartheta(y_j^-)|,
\tag{24}
\]

as long as `x` remains in that phase. Therefore

\[
\boxed{
M_j(x)\le E_b(x)+E_b(y_j).
}
\tag{25}
\]

Apply Stieltjes/Abel summation with weight `1/t` on that phase. If its right endpoint is `z_j` (possibly infinity), then (25) gives

\[
\sum_{q\text{ in phase }j}
|c_q|\frac{\log q}{q}
\ll_b
 e^{-bV(y_j)}
+
\int_{y_j}^{z_j}e^{-bV(t)}\frac{dt}{t}.
\tag{26}
\]

The endpoint at infinity vanishes because `M_j(x)/x` is bounded by `O(e^{-bV(x)}+E_b(y_j)/x)`. For a finite phase, the right boundary contributes only another `O_b(e^{-bV(y_j)})`, since `V` is eventually increasing.

Summing (26) over the disjoint sign phases, the integrals do **not** acquire an `M` factor: they concatenate into one tail integral. Only the phase-reset boundary terms pay per alternation. Thus

\[
\boxed{
\sum_{q\ge Y}|c_q|\frac{\log q}{q}
\ll_b
\left(
M+\ell_{\rm KV}(Y)
\right)e^{-bV(Y)}.
}
\tag{27}
\]

Here we used the same elementary Laplace estimate as `RE-176`,

\[
\int_Y^\infty e^{-bV(t)}\frac{dt}{t}
=
\left(\frac5{3b}+o(1)\right)
\ell_{\rm KV}(Y)e^{-bV(Y)}.
\tag{28}
\]

Equation (27) is the quantitative reason repeated signs help only linearly. Each new phase may reset the hidden cumulative discrepancy once, buying one additional local boundary allowance `e^{-bV(Y)}`; it does not recreate the whole integrated KV tail.

## 3. The centered Euler kernel costs no more than first-slope variation

It remains to compare (20) with (27). Because the positive phase lies below `Y`, (11) gives, for large `p`,

\[
a_P\le 2\log Y.
\tag{29}
\]

For every prime `q>=Y`,

\[
B(q)\le\frac{2\log q}{q},
\qquad
H(q)\le\frac2q,
\tag{30}
\]

so

\[
|K_P(q)|
\le B(q)+a_PH(q)
\le C\frac{\log q}{q}
\tag{31}
\]

with an absolute constant `C`. Consequently,

\[
\left|\sum_{q\ge Y}c_qK_P(q)\right|
\le
C\sum_{q\ge Y}|c_q|\frac{\log q}{q}.
\tag{32}
\]

Combine (20), (27), and `d_p asymp (sqrt(p) log p)^(-1)`:

\[
\frac1{\sqrt p\log p}
\ll_{b,\lambda}
\left(M+\ell_{\rm KV}(Y)\right)e^{-bV(Y)}.
\tag{33}
\]

This is exactly (6).

A useful feature of the proof is that arbitrary integer magnitudes are allowed inside every phase. The tariff depends on **sign complexity**, not support cardinality or coefficient size. Dense packets, sparse packets, and infinite final phases are all covered as long as the number of sign changes after `Y` is finite.

## 4. Distance-complexity tradeoff

Taking logarithms in (6) gives

\[
bV(Y)
\le
\frac12\log p
+
\log\log p
+
\log\bigl(M+\ell_{\rm KV}(Y)\bigr)
+O_{b,\lambda}(1).
\tag{34}
\]

The inversion of the KV coordinate used in `RE-176` implies

\[
\log\ell_{\rm KV}(Y)=o(V(Y)).
\tag{35}
\]

Therefore, if `M=p^{o(1)}`, equation (34) first forces `V(Y)=O_b(log p)` and then

\[
\log(M+\ell_{\rm KV}(Y))=o(\log p),
\tag{36}
\]

which proves (7).

More generally, if

\[
M=p^{\kappa+o(1)}
\tag{37}
\]

for some fixed `kappa>=0`, then

\[
\boxed{
bV(Y)\le
\left(\frac12+\kappa+o(1)\right)\log p.}
\tag{38}
\]

Conversely, at any fixed excess `delta>0`, (6) and (35) show that (8) forces

\[
M
\gg
\frac{e^{bV(Y)}}{\sqrt p\log p}
-
\ell_{\rm KV}(Y)
=
p^{\delta-o(1)},
\tag{39}
\]

which is (9). Thus the escape has acquired a genuine complexity law: every extra polynomial factor in the number of sign phases buys at most the corresponding additive amount in the `bV` exponent.

## 5. Adversarial checks and exact scope

**Finite sign complexity is essential.** The proof sums one boundary-reset allowance per sign phase. If the tail changes sign infinitely often, the right side of (27) can be infinite and the theorem gives no obstruction. The surviving architecture is therefore not merely “more than two sign changes”; it is a tail whose oscillation complexity grows fast enough with `p`, potentially without finite variation in sign.

**The first positive phase must be completed before `Y`.** The centered debt (16) uses its barycenter `a_P`. If positive and negative coefficients are already interlaced before the chosen cutoff, there is no single first-phase barycenter to which (20) applies. One can always place `Y` at the first subsequent sign change, but the theorem does not control architectures that start high-frequency alternation immediately after the deletion packet with no separated positive phase.

**Two-jet matching remains extra information.** Nothing here proves that the original Robin problem supplies `D_Q'(1+)=0`. As in `RE-175`--`RE-176`, the theorem asks what that source invariant would buy if available. Closing Robin still requires deriving selector-relevant boundary information from genuine arithmetic input rather than imposing it on matched controls.

**No bounded-multiplicity assumption is hidden.** The coefficients may have arbitrary integer size. Equation (25) converts the KV envelope itself into a bound on the absolute mass accumulated during a sign-constant phase.

**Absolute convergence is not an extra tail hypothesis.** For finite `M`, (27) proves absolute convergence of the tail first-slope variation. The Mertens tail is smaller by an additional logarithmic factor. Hence the two exact boundary coordinates used in (15) are compatible with the stated capacity assumptions.

**The theorem is a necessary condition, not a construction.** A tail with `p^delta` sign phases inside the enlarged horizon is not shown to exist. Ordinary-prime discreteness, exact integer realization, and simultaneous control of further Euler jets may impose additional costs.

## 6. Representation audit

The capacity lemma (27) is generic. It is an Abel-summation statement for a signed cumulative source constrained by a decreasing normalized envelope; replacing primes by another ordered atomic source with the same cumulative bound would give the same `M + ell` law. The use of maximal sign-constant phases is also representation-stable under regrouping zero coefficients: only actual sign reversals matter.

The line-specific content enters in three places. First, the Robin matched-control construction supplies a deletion debt `d_p asymp (sqrt(p) log p)^(-1)` at the selector scale. Second, the Euler boundary coordinates provide the exact pair `H(q),B(q)` and the centered identity (16). Third, the ordinary-prime Chebyshev discrepancy is the source quantity governed by the KV envelope. The theorem should therefore be read as a **source-complexity tariff for a specific Robin-scale Euler debt**, not as a new theorem about KV decay by itself.

The result is also not coefficient recovery. High-temperature Euler rigidity in `RE-174` identifies every changed prime but is exponentially ill-conditioned. Here only two scalar boundary coordinates are used; what they recover is not the tail, but a lower bound on the amount of sign-phase complexity required to hide its residual workload far away.

## 7. Prior-art audit

The analytic mechanism in (26)--(27) is classical Abel/Stieltjes summation, and the general study of sign changes and variation-diminishing transforms is classical. Those facts are background rather than a novelty claim. A broad search did not identify the specific combination used here: a finite-sign decomposition of a KV-controlled prime-source discrepancy, centered Euler boundary-jet debt, and the resulting selector-normalized `M + ell_KV` tradeoff.

No new external theorem is load-bearing. The KV source envelope and its asymptotic tail integral were already anchored and derived in the line, most recently in `RE-176`. Therefore `SOURCES.md` requires no change.

## 8. Consequence for the research frontier

`RE-176` left “add more alternations” as the most immediate compact escape. `RE-177` makes that escape quantitative. If the later repair uses only finitely many, polylogarithmically many, or any `p^{o(1)}` sign phases, the leading first-slope horizon remains

\[
bV(Y)\le\left(\frac12+o(1)\right)\log p.
\tag{40}
\]

To cross to `bV(Y)=(1/2+delta)log p`, the repair must already have at least `p^{delta-o(1)}` sign phases. The next source-side question is therefore narrower: can an ordinary-prime integer control with **polynomial or infinite sign complexity** realize the required exact boundary matching while staying inside the KV envelope and preserving the selector-scale excursion, or do higher boundary jets/ordinary-prime granularity impose another complexity tariff?

Even a negative answer would still not make the boundary slope intrinsic to Robin. The separate arithmetic task remains to connect whichever finite Euler-jet information is used to the actual ordinary-prime source rather than grant it as a matched-control constraint.