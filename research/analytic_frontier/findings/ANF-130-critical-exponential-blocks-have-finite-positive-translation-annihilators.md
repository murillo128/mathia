# ANF-130 — critical exponential blocks have finite positive translation annihilators

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SECOND-GENERATION-TRANSLATION-EXCISION + FINITE-POSITIVE-ANNIHILATOR + ARBITRARY-POLYNOMIAL-SOURCE-SUPPRESSION + SECOND-EXPONENTIAL-NOTCH-BUDGET + GLOBAL-COMPLETION-GATE`. `ANF-129` shows that a fixed-`q` exponential digit cloud can cancel the original `ANF-115` saddle while retaining bounded macroscopic Montgomery--Taylor source mass, exponentially negligible affine cardinality, and exponentially negligible fixed-notch mass. That removes the source-blowup obstruction left by `ANF-127`--`ANF-128`, but it does not make the critical block an essential near-extremizer component by itself.

For every such fixed-`q` critical block, its regenerated source landscape has only finitely many nondegenerate global maxima. A positive finite translation polynomial can be chosen to vanish at all of them simultaneously. Multiplying the block by that polynomial is a completely physical operation: it is just a finite union of real translates with positive integer multiplicities. One zero at each source maximum reduces the complete source norm by `O(A^{-1})`; repeating the finite annihilator `m` times gives `O(A^{-m})` for every fixed `m`. Hence the critical exponential block admits an explicit same-profile companion which mirrors its **entire** source vector asymptotically, but the block plus that companion is globally excisable.

More generally, every subexponential outer translation cloud of the critical block obeys a second-generation version of `ANF-122`/`ANF-126`: if it cancels on widening Gaussian neighborhoods of all regenerated source maxima, then its complete source norm, fixed-notch norm, and affine size are negligible on the `ANF-129` packet scale. Conversely, if the outer translation orbit itself is required to carry macroscopic central-notch mass, it must cross a **second positive exponential copy-budget threshold**. Thus `ANF-129` does not by itself produce a fatal completion; within its own translation orbit, the live escape is pushed to another exponential layer or to a genuinely profile-transverse companion.

## 1. The `ANF-129` block has a finite Gaussian source skeleton

Fix `gamma>0` and the `ANF-115` packet

\[
P_A=P_{A,\lfloor\gamma A\rfloor},
\qquad
E_A=E_0(P_A),
\qquad
a=a_\gamma,
\qquad
f=F_\gamma(a),
\]

with

\[
F_\gamma(\alpha)
=\alpha+2\gamma\log\cos\frac{\pi\alpha}{2}.
\tag{1}
\]

Fix a sufficiently large integer `q` in the critical construction of `ANF-129`. Write

\[
D_q(x)=\sum_{v=0}^{q-1}e^{-2\pi i vx},
\qquad
d_q=\frac{q-1}{qa},
\]

and let `r_q>0` be the critical repetition density for which

\[
\Psi_q(\alpha)
:=F_\gamma(\alpha)-f
+2r_q\log|D_q(d_q\alpha)|
\tag{2}
\]

has

\[
\sup_{0\le\alpha<1}\Psi_q(\alpha)=0.
\tag{3}
\]

Let `X_A` denote the physical critical cloud `T_A` of `ANF-129`, with `h_A=floor(r_qA)` digit levels and the `O(A^{-4})` distinctness perturbations of the digit spacings. That finding proves

\[
0<c_q\le\frac{E_0(X_A)}{E_A}\le C_q<\infty,
\tag{4}
\]

and, for every fixed notch width `0<eta<a` after choosing `q` large enough,

\[
E_\eta(X_A)=e^{-\Omega_q(A)}E_A,
\qquad
|X_A|=e^{-\Omega_q(A)}E_A.
\tag{5}
\]

The critical set

\[
\mathcal K_q^+
:=\{\alpha\in(0,1):\Psi_q(\alpha)=0\}
=\{\alpha_1,\ldots,\alpha_J\}
\tag{6}
\]

is finite and nonempty. `ANF-129` proves that on every interval between consecutive zeros of `D_q`, `Psi_q` is strictly concave, and that every global critical point is an interior nondegenerate maximum. Since `q` is fixed throughout the `A->infinity` family, there are constants `epsilon_q,c_q',C_q'>0` such that

\[
\Psi_q(\alpha)
\le
-c_q'\operatorname{dist}(\alpha,\mathcal K_q^+)^2
\tag{7}
\]

whenever `dist(alpha,K_q^+)<epsilon_q`, while

\[
\Psi_q(\alpha)\le-c_q'
\tag{8}
\]

outside those fixed neighborhoods and the corresponding reflected neighborhoods on `[-1,0]`.

The floor in `h_A` changes the logarithmic amplitude by only `O_q(1)` near the critical set, and the `O(A^{-4})` spacing perturbations change `log|p_A|` there by `o(1)`. The same is true of the harmless `ANF-115` physical distinctness perturbation. Therefore the exact source density of `X_A` inherits a uniform Gaussian concentration estimate: for

\[
\mathcal B_A(U)
:=
\left\{
\alpha\in[-1,1]:
\operatorname{dist}(|\alpha|,\mathcal K_q^+)
\le\frac{U}{\sqrt A}
\right\},
\tag{9}
\]

there are constants `C,c>0`, depending only on the fixed `q,gamma`, such that

\[
\boxed{
\frac{E_{\mathcal B_A(U)^c}(X_A)}{E_A}
\le Ce^{-cU^2}
}
\tag{10}
\]

for

\[
1\le U\le\epsilon_q\sqrt A.
\]

The same local comparison gives, for every fixed integer `m>=1`,

\[
\boxed{
\frac1{E_A}
\int_{-1}^{1}
\operatorname{dist}(|\alpha|,\mathcal K_q^+)^{2m}
J_0(\alpha)|S_{X_A}(\alpha)|^2\,d\alpha
=O_{q,m}(A^{-m}).
}
\tag{11}
\]

Equation (11) is just the Gaussian moment scale of the finitely many nondegenerate critical chambers. It is the extra information needed to go beyond the original-saddle excision theorem: internally `X_A` was built with an exponential number of copies, but **after critical tuning its complete source norm again lives on a finite Gaussian skeleton**.

## 2. Every subexponential outer mirror is excisable

Take an arbitrary positive outer translation cloud of `X_A`, containing one distinguished untranslated copy,

\[
Y_A
:=
\bigsqcup_{j=0}^{J_A}w_{j,A}(X_A+\tau_{j,A}),
\qquad
w_{0,A}=1,
\qquad
\tau_{0,A}=0,
\tag{12}
\]

and put

\[
Q_A(\alpha)
:=\sum_{j=0}^{J_A}w_{j,A}e^{-2\pi i\alpha\tau_{j,A}},
\qquad
V_A:=\sum_jw_{j,A}.
\tag{13}
\]

Translation gives the exact factorization

\[
S_{Y_A}(\alpha)=Q_A(\alpha)S_{X_A}(\alpha),
\qquad
|Q_A(\alpha)|\le V_A.
\tag{14}
\]

Assume only

\[
\boxed{
\log(e+V_A)=o(A).
}
\tag{15}
\]

Choose `U_A->infinity` with

\[
U_A^2=o(A),
\qquad
\log(e+V_A)=o(U_A^2).
\tag{16}
\]

Splitting the exact source integral over `B_A(U_A)` and its complement, then using (10) and (14), gives

\[
\boxed{
\frac{E_0(Y_A)}{E_A}
\le
\frac{E_{\mathcal B_A(U_A)}(Y_A)}{E_A}
+C V_A^2e^{-cU_A^2}.
}
\tag{17}
\]

The second term tends to zero by (16). Hence

\[
\boxed{
E_{\mathcal B_A(U_A)}(Y_A)=o(E_A)
\quad\Longrightarrow\quad
E_0(Y_A)=o(E_A).
}
\tag{18}
\]

This is a second-generation translation-orbit excision theorem. `ANF-126` cannot be applied directly to the internal construction of `X_A`, because its unsigned packet budget is `exp(rho_q A+o(A))`; (18) instead starts **after** that exponential layer has been critically tuned to bounded macroscopic source mass. Once the new finite set of regenerated source maxima has formed, every successful outer mirror with subexponential copy budget again collapses globally.

The fixed-notch and affine conclusions are equally automatic. Define the exact critical-landscape notch gap

\[
G_{q,\eta}
:=-\sup_{0\le\alpha\le\eta}\Psi_q(\alpha).
\tag{19}
\]

If

\[
\Delta_\eta
:=f-\sup_{0\le\alpha\le\eta}F_\gamma(\alpha),
\]

then `|D_q|<=q` and `rho_q=r_q log q` give

\[
\boxed{
G_{q,\eta}
\ge\Delta_\eta-2\rho_q>0
}
\tag{20}
\]

for the large-`q` choice already made in `ANF-129`. The exact physical perturbations do not change this exponential rate, so

\[
\frac{E_\eta(X_A)}{E_A}
\le
\exp[-G_{q,\eta}A+o(A)].
\tag{21}
\]

Consequently, under (15),

\[
\boxed{
E_\eta(Y_A)=o(E_A).
}
\tag{22}
\]

Also, from `ANF-129`,

\[
\frac1A\log\frac{|X_A|}{E_A}
=
-\kappa_q+o(1),
\qquad
\kappa_q
:=\gamma\log2+f-\rho_q>0.
\tag{23}
\]

Therefore

\[
\boxed{|Y_A|=V_A|X_A|=o(E_A)}
\tag{24}
\]

whenever (15) holds.

If a Montgomery--Taylor near-extremizer decomposes as

\[
W_A=Y_A\sqcup R_A,
\qquad
\frac{E_0(W_A)}{L_A}=1+o(1),
\qquad
0<\lambda\le\frac{E_A}{L_A}\le\Lambda,
\tag{25}
\]

and the outer cloud satisfies the mirror condition in (18), then (18), (22), (24), the Hilbert triangle inequality, and `L(R_A)=L_A+o(L_A)` give

\[
\boxed{
\frac{E_0(R_A)}{L(R_A)}\to1,
\qquad
\frac{E_\eta(R_A)-E_\eta(W_A)}{L_A}\to0.
}
\tag{26}
\]

Thus a subexponential translation-orbit mirror of the critical exponential block is globally irrelevant to the exposure envelope `beta_eta` of `ANF-099`.

## 3. A finite positive annihilator realizes full-source mirroring explicitly

The implication (18) is not vacuous. Because `K_q^+` is finite and all its points are positive, set

\[
\tau_j:=\frac1{2\alpha_j},
\qquad 1\le j\le J,
\tag{27}
\]

and define

\[
Q_q(\alpha)
:=
\prod_{j=1}^{J}
\left(1+e^{-2\pi i\tau_j\alpha}\right).
\tag{28}
\]

For every `j`,

\[
Q_q(\alpha_j)=Q_q(-\alpha_j)=0.
\tag{29}
\]

More importantly, `Q_q` has a completely physical positive expansion. Expanding the product gives

\[
Q_q(\alpha)
=
\sum_{I\subseteq\{1,\ldots,J\}}
 e^{-2\pi i\alpha\sum_{j\in I}\tau_j},
\tag{30}
\]

so its coefficients are positive integers after coincident subset sums are collected. It is exactly the modulation factor of `2^J` translated copies of `X_A`, counted with multiplicity. No signed weight or abstract Hilbert vector is used.

For any fixed integer `m>=1`, use the positive polynomial

\[
Q_{q,m}(\alpha):=Q_q(\alpha)^m.
\tag{31}
\]

It has a zero of order at least `m` at every point of the symmetric critical set. The corresponding physical outer cloud `Y_A^{(m)}` contains

\[
V_{q,m}=2^{mJ}
\tag{32}
\]

copies of `X_A`, independent of `A`. Near the critical set,

\[
|Q_{q,m}(\alpha)|^2
\le
C_{q,m}
\operatorname{dist}(|\alpha|,\mathcal K_q^+)^{2m},
\tag{33}
\]

while it is bounded globally by `V_{q,m}^2`. Combining (11), the fixed exponential gap away from the critical neighborhoods, and (33) yields

\[
\boxed{
\frac{E_0(Y_A^{(m)})}{E_A}
=O_{q,m}(A^{-m}).
}
\tag{34}
\]

Thus a constant-size positive translation architecture can suppress the complete source vector of the internally exponential block to **any prescribed fixed polynomial order**.

Let

\[
Y_A^{(m)}=X_A\sqcup U_A^{(m)},
\tag{35}
\]

where `U_A^{(m)}` consists of all nonconstant translation terms in (31). From (4) and (34),

\[
\|S_{X_A}+S_{U_A^{(m)}}\|_0
=o(\sqrt{E_A}).
\tag{36}
\]

The reverse triangle inequality then gives

\[
E_0(U_A^{(m)})
=E_0(X_A)+o(E_A),
\tag{37}
\]

and expanding (36) gives

\[
\boxed{
\mathcal C_0(X_A,U_A^{(m)})
=-E_0(X_A)+o(E_A).
}
\tag{38}
\]

This is stronger than local saddle mirroring: `U_A^{(m)}` is an explicit positive physical companion whose complete Montgomery--Taylor source vector converges to `-S_{X_A}`. Yet by (34), (22), and (24), the combined block `X_A sqcup U_A^{(m)}` is excisable. The same phenomenon found in `ANF-122` for a subexponential same-saddle packet cloud therefore reappears **after** the first critical exponential modulation layer.

## 4. Making the translation orbit notch-bright costs a second exponential layer

The same pointwise estimate `|Q_A|<=V_A` gives a quantitative lower bound on any attempt to use outer translations of `X_A` themselves as the central-notch-efficient component. From (21),

\[
\frac{E_\eta(Y_A)}{E_A}
\le
V_A^2\exp[-G_{q,\eta}A+o(A)].
\tag{39}
\]

Therefore, if for some `c>0`

\[
E_\eta(Y_A)\ge cE_A
\tag{40}
\]

along a subsequence, then necessarily

\[
\boxed{
\liminf_{A\to\infty}
\frac1A\log V_A
\ge
\frac{G_{q,\eta}}2
>0.
}
\tag{41}
\]

A finite, polynomial, or arbitrary subexponential outer translation orbit is therefore incapable of doing both jobs: it may mirror the critical block, but it cannot also supply macroscopic central-notch energy. To make the orbit itself notch-bright requires a **second exponential copy budget**.

This budget law is not, by itself, a contradiction with affine near-extremality. Indeed, at `alpha=0`,

\[
\Psi_q(0)=-f+2\rho_q,
\]

so

\[
G_{q,\eta}
\le f-2\rho_q.
\tag{42}
\]

Combining (23) and (42),

\[
\frac{G_{q,\eta}}2
\le
\frac f2-\rho_q
<
\gamma\log2+f-\rho_q
=\kappa_q.
\tag{43}
\]

Hence there is exponential-rate room, at least at the crude cardinality level, for an outer translation cloud to cross the notch-brightness threshold while still satisfying `|Y_A|=o(E_A)`. The result therefore does **not** close the exponential route. It identifies its next unavoidable scale without pretending that the affine budget already kills it.

## 5. Adversarial controls and exact scope

Several possible overstatements were checked.

First, the positive annihilator does not contradict `ANF-129`. The internal cloud `X_A` has an exponential unsigned packet budget and escapes the original-saddle excision of `ANF-126` by regenerating source at new critical maxima. `ANF-130` begins only after that regeneration has been critically tuned to bounded macroscopic source mass. The new outer annihilator cancels those regenerated maxima rather than the original `ANF-115` saddle.

Second, no claim is made about an arbitrary physical companion. Equations (18), (34), and (41) concern the positive **translation orbit of the complete critical block**. A genuinely profile-transverse component can carry source and notch mass with a different landscape; that is still the principal global completion route left by `ANF-120`, `ANF-123`, and `ANF-129`.

Third, the fixed-`q` hypothesis matters. The number of critical maxima, their separation, and their nondegenerate curvatures are all fixed before `A->infinity`. If `q=q(A)` grows, maxima can move, proliferate, or coalesce and the constants in (10)--(11), the number of annihilating factors in (28), and the outer copy count in (32) need not remain uniform. The moving-arity regime of `ANF-128` is therefore not collapsed by this finding.

Fourth, (34) uses the fact that `E_0(X_A)=Theta(E_A)`. A fixed-order zero only buys a polynomial Gaussian factor `A^{-m}`. It would not excise the exponentially oversized reservoirs of `ANF-127`--`ANF-128`; suppressing an `exp(cA)` source excess by increasing the annihilator order changes the copy-budget analysis and belongs to the exponential cascade problem rather than to the bounded-source critical branch settled here.

Finally, the construction needs no distinctness assumption for the outer translated copies. Coincident subset sums in (30) simply combine into positive integer multiplicities, which are admissible physical multisets. Real translation preserves conjugation invariance.

## 6. Prior-art boundary and new live gate

The local analytic ingredients are classical. NIST DLMF §2.3 records Laplace's method for finitely many nondegenerate real maxima, and the classical theory also treats amplitudes that vanish to finite order at a maximizing point; this is exactly the generic reason that a zero of order `m` produces an additional `A^{-m}` factor in a Gaussian Laplace integral. Prescribed-zero questions for nonnegative trigonometric polynomials are also classical, for example S. Ruscheweyh, *Non-Negative Trigonometric Polynomials with Constraints*, Z. Anal. Anwend. 5 (1986), 169--177. Generalized Riesz-product literature supplies neighboring language for products of trigonometric factors.

None of those sources is load-bearing for the Mathia claim. The annihilator (28) is an explicit elementary product, its positive-translation realization is the exact expansion (30), and the Gaussian moment estimate follows directly from the source landscape already proved in `ANF-129`. The new content is the coupling of those facts to Montgomery--Taylor source mirroring, fixed-notch darkness, affine excision, and the second exponential notch-budget law (41). No new durable dependency is therefore required in `research/analytic_frontier/SOURCES.md`.

The global gate is now sharper. The bounded-source critical exponential block of `ANF-129` is **not** protected from physical anti-alignment by its internal exponential complexity: a finite positive translation companion can mirror it arbitrarily well on the source scale, but that mirror self-destructs and is deleted from the near-extremizer. A translation-orbit completion that also supplies macroscopic notch exposure must pay another positive exponential rate. Thus a fatal completion must either build a genuinely profile-transverse notch-bright companion, or analyze a second critical exponential modulation layer whose new source landscape survives the same excision test. No clue disposition changes are justified by this result.