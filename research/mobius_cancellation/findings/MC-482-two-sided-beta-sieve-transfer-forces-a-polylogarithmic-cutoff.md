# MC-482 — Two-sided beta-sieve transfer forces a polylogarithmic cutoff

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

There is a genuinely independent signed-surrogate mechanism for the exact pair-sieve mask left open by `MC-481`: bracket the hard mask between classical lower and upper beta-sieve divisor sums and use their midpoint. Unlike centered Selberg leakage, the resulting replacement error is bounded pointwise by the **upper-minus-lower sieve gap**, so its transfer cost can be estimated from local divisibility counts without first estimating the original twisted hard-mask discrepancy.

That mechanism nevertheless has a sharp level-versus-accuracy tariff on the actual short source interval. In the standard fundamental-lemma bookkeeping, conductor-power relative accuracy forces the sieve cutoff to be only polylogarithmic in the source conductor. In particular, a fixed-power cutoff `z >= p^alpha` cannot be transferred with a `p^{-eta}` relative gain by this phase-blind upper/lower sandwich when the source interval has polynomial length `H <= p^theta`.

Keep the prime-conductor pair-sieve setup of `MC-471`--`MC-481`. Let

\[
A_z(n):=\mathbf 1_{(n(n+h),P(z))=1},
\qquad
K_h(n):=\chi(n+h)\overline{\chi(n)},
\]

with the same parity-degenerate and conductor primes removed from `P(z)`, so that the local pair sieve is admissible and `(P(z),p)=1`. For squarefree `d|P(z)`, write

\[
\nu_h(d):=\#\{a\pmod d:d\mid a(a+h)\}.
\]

Then `nu_h` is multiplicative and at an active prime `q`,

\[
\nu_h(q)=
\begin{cases}
1,&q\mid h,\\
2,&q\nmid h.
\end{cases}
\tag{1}
\]

Thus the local density is

\[
g_h(d)=\frac{\nu_h(d)}d,
\qquad
V_h(z)=\prod_{q<z}\left(1-\frac{\nu_h(q)}q\right),
\tag{2}
\]

and the standard sieve-dimension condition holds with `kappa=2` (primes dividing `h` only decrease the local density relative to the generic two-residue case).

Let `lambda_d^+` and `lambda_d^-` be classical upper and lower beta-sieve weights of level `D`, supported on squarefree divisors of `P(z)`, with `|lambda_d^pm|<=1`, and put

\[
s:=\frac{\log D}{\log z}.
\tag{3}
\]

Define

\[
B^\pm(n):=\sum_{d\mid n(n+h)}\lambda_d^\pm,
\qquad
B(n):=\frac{B^+(n)+B^-(n)}2.
\tag{4}
\]

The defining beta-sieve inequalities give pointwise

\[
B^-(n)\le A_z(n)\le B^+(n),
\]

hence

\[
\boxed{
|A_z(n)-B(n)|\le \frac{B^+(n)-B^-(n)}2.
}
\tag{5}
\]

Therefore, for every interval `I` of length `H` and every coefficient with `|K(n)|<=1` -- in particular `K=K_h` -- one has the **independent transfer inequality**

\[
\boxed{
\left|\sum_{n\in I}K(n)(A_z(n)-B(n))\right|
\le
\frac12\sum_{n\in I}(B^+(n)-B^-(n)).
}
\tag{6}
\]

For the interval sequence, CRT gives exactly

\[
N_d(I):=\#\{n\in I:d\mid n(n+h)\}
=
H\frac{\nu_h(d)}d+r_d(I),
\qquad
|r_d(I)|\le \nu_h(d).
\tag{7}
\]

The beta-sieve fundamental lemma gives, once `s` is sufficiently large in terms of the dimension,

\[
\sum_{d|P(z)}\lambda_d^\pm\frac{\nu_h(d)}d
=
V_h(z)\left(1+O(s^{-s/2})\right).
\tag{8}
\]

Using `(7)` in the two divisor sums, subtracting them, and using `|lambda_d^+-lambda_d^-|<=2` yields

\[
\sum_{n\in I}(B^+(n)-B^-(n))
\ll
H V_h(z)s^{-s/2}
+
\sum_{\substack{d\le D\\d|P(z)}}\nu_h(d).
\tag{9}
\]

Since `nu_h(d)<=2^{omega(d)}<=tau(d)` and

\[
\sum_{d\le D}2^{\omega(d)}\ll D\log(2D),
\tag{10}
\]

we obtain the concrete source-interval transfer bound

\[
\boxed{
\left|\sum_{n\in I}K(n)(A_z(n)-B(n))\right|
\ll
H V_h(z)s^{-s/2}+D\log(2D).
}
\tag{11}
\]

Equation `(11)` is the useful new accounting statement. It is not the target-equivalent identity closed by `MC-481`: its right side depends only on the beta-sieve main-term gap and the elementary interval distribution of the local congruence classes, not on `sum K_h A_z`.

However, `(11)` also shows why the most obvious version cannot pay the current conductor-power budget. Suppose one tries to certify from the standard fundamental-lemma and absolute-remainder bounds that

\[
\left|\sum_{n\in I}K(n)(A_z(n)-B(n))\right|
\ll H V_h(z)p^{-\eta}
\tag{12}
\]

for some fixed `eta>0`, with

\[
H\le p^\theta
\tag{13}
\]

for fixed `theta>0`. Making the first term of `(11)` power-small by this bookkeeping requires

\[
s^{-s/2}\ll p^{-\eta},
\]

hence

\[
\boxed{
s\log s\ge (2\eta+o(1))\log p,
\qquad
s\ge(2\eta+o(1))\frac{\log p}{\log\log p}.
}
\tag{14}
\]

The interval remainder in `(11)` simultaneously requires, at the same proof level,

\[
D\log(2D)\ll H V_h(z)p^{-\eta}\le p^{\theta-\eta},
\tag{15}
\]

so

\[
s\log z=\log D\le(\theta-\eta+o(1))\log p.
\tag{16}
\]

Combining `(14)` and `(16)` gives the necessary cutoff condition

\[
\boxed{
\log z
\le
\left(\frac{\theta-\eta}{2\eta}+o(1)\right)\log\log p,
}
\tag{17}
\]

whenever `theta>eta`. Thus this standard two-sided fundamental-lemma transfer can only certify a fixed conductor-power relative gain in a **polylogarithmic-cutoff regime**,

\[
z\le(\log p)^{O_{\theta,\eta}(1)}.
\tag{18}
\]

For every fixed `alpha>0`, a polynomial cutoff `z>=p^alpha` contradicts `(14)`--`(16)`: the remainder bound forces `s=O_{alpha,theta,eta}(1)`, while power accuracy of the fundamental-lemma term requires `s to infinity` at order `log p/log log p`.

There is an immediate specialization to the exact empty-vector sieve of `MC-470`. Lichtman's construction has

\[
Q=D_0^\varepsilon,
\qquad
z=D_0^{\varepsilon^2}=Q^\varepsilon,
\]

so if one adds the standard lower beta-sieve companion at the **same level `Q`**, then

\[
s=\frac{\log Q}{\log z}=\frac1\varepsilon.
\tag{19}
\]

With the construction parameter `epsilon` fixed, the fundamental-lemma accuracy supplied by `(8)` is therefore a fixed quantity of size

\[
s^{-s/2}=\varepsilon^{1/(2\varepsilon)},
\tag{20}
\]

not a negative power of `p`. The same-level upper/lower companion is a valid signed surrogate, but the classical fundamental-lemma guarantee alone does not turn it into a conductor-power replacement. Raising the sieve level to make `s` grow immediately reintroduces the interval-level cost quantified by `(15)`--`(18)`.

This does **not** prove that every two-sided sieve transfer fails. It isolates exactly what extra structure would be needed to beat `(11)`: cancellation in the interval remainders before absolute values, a stronger distribution theorem for the pair-sieve congruence sequence up to levels beyond the interval-length barrier, a phase-coupled treatment that does not discard `K_h` in `(6)`, or a source regime in which the active cutoff is genuinely only polylogarithmic in `p`.

## 1. Pointwise bracketing creates an independent replacement mechanism

The beta-sieve upper/lower inequalities are purely combinatorial. Applied to the small-prime kernel of `n(n+h)`, they give

\[
B^-(n)\le \mathbf 1_{(n(n+h),P(z))=1}\le B^+(n)
\]

before any character sum is considered. Taking the midpoint proves `(5)`.

This is structurally different from the current Selberg envelope. For `L=beta-A`, `MC-481` showed that after canonical centering one has exactly `D_L=D_beta-D_A`, so estimating centered leakage is already the original hard-mask problem modulo a controlled comparison term. Equation `(6)` instead dominates the **pointwise absolute replacement error** by a separate nonnegative sieve gap. If that gap were power-small on the source interval, the transfer would be complete without estimating `D_A` first.

So the upper/lower sandwich is a legitimate answer to one half of the accepted clue's decisive test: it supplies a new exact structure that is independently priceable. The obstruction is quantitative rather than algebraic.

## 2. The short interval, not the complete local period, creates the level tariff

For each squarefree `d|P(z)`, the congruence

\[
d\mid n(n+h)
\]

occupies exactly `nu_h(d)` residue classes modulo `d`. An interval of length `H` therefore meets those classes with count `(7)`, with at most one endpoint error per residue class.

After summing with the two beta-sieve weights, the main terms are governed by the classical fundamental lemma `(8)`. The endpoint terms have no supplied sign cancellation once `(6)` has already discarded the character phase. The generic safe estimate is therefore

\[
\sum_{d\le D}\nu_h(d).
\]

For squarefree `d`, `nu_h(d)<=2^{omega(d)}`. The elementary identity

\[
2^{\omega(d)}=\sum_{e|d}\mu^2(e)
\]

implies

\[
\sum_{d\le D}2^{\omega(d)}
\le
D\sum_{e\le D}\frac{\mu^2(e)}e
\ll D\log(2D),
\]

which proves `(10)` and `(11)`.

On the complete sieve period the `r_d` terms vanish, but that does not solve the live problem: `MC-477` works on source intervals `H<=p`, while the primorial pair-sieve period is vastly larger in the polynomial-cutoff regime. As in `MC-479`, complete-period smallness cannot be promoted to every short source interval without an additional distribution theorem.

## 3. Fixed-power cutoffs and conductor-power accuracy pull the sieve depth in opposite directions

The first term of `(11)` gets better only by increasing the beta-sieve depth `s=log D/log z`. The second term gets worse because increasing `s` raises the supported divisor level `D=z^s`.

For fixed conductor-power target `p^{-eta}`, the fundamental lemma needs roughly

\[
s\asymp\frac{\log p}{\log\log p}
\]

before its generic `s^{-s/2}` error reaches the target. If `z=p^alpha`, that choice gives

\[
D=z^s
=
\exp\!\left(\Omega\!\left(\frac{(\log p)^2}{\log\log p}\right)\right),
\]

far beyond any polynomial source interval. Conversely, keeping `D` below a polynomial interval when `z=p^alpha` forces `s=O(1)`, which leaves only fixed fundamental-lemma accuracy.

The obstruction is not "sieve theory cannot approximate roughness." It is more precise: **the standard phase-blind beta-sieve sandwich cannot simultaneously make its fundamental-lemma gap conductor-power small and keep the divisor level within a polynomial short interval when the active cutoff itself is a fixed conductor power.**

Equation `(17)` marks the surviving scale: polylogarithmic `z` is necessary for this particular certification strategy, though not sufficient. Even there one still has to check the exact source depth, `V_h(z)`, endpoint costs, the envelope comparison scale from `MC-478`, and the outer Fejer/coefficient-normalization tariffs.

## 4. Prior art and novelty boundary

John Friedlander and Henryk Iwaniec, *Opera de Cribro*, American Mathematical Society Colloquium Publications 57 (2010), Sections 6.4--6.5 and Lemma 6.11, develop the beta-sieve upper/lower weights and the fundamental lemma used in `(8)`. Pär Kurlberg, Stephen Lester and Lior Rosenzweig, *Superscars for arithmetic point scatters II*, Forum of Mathematics, Sigma 11 (2023), e37, DOI `10.1017/fms.2023.33`, Section 2.1, states the needed modern form explicitly: upper and lower beta-sieve weights of level `D` are `1`-bounded, and for sieve dimension `kappa` their main sums equal `V(z)(1+O(s^{-s/2}))` once `s` is sufficiently large. That paper cites Friedlander--Iwaniec for the theorem.

Andrew Granville and Dimitris Koukoulopoulos, Chapter 19 *The Fundamental Lemma of Sieve Theory* in their prime-number-theory text, likewise formulates the pointwise upper/lower sieve-weight inequalities and level support that underlie `(5)`--`(6)`.

No novelty is claimed for beta-sieve bracketing, the fundamental lemma, the divisor bound `sum 2^{omega(d)} << D log D`, or the generic level-of-distribution remainder. The Mathia-specific delta is the **source-frame transfer accounting**: applying the classical two-sided bracket to the exact translated pair-sieve target of `MC-471` gives the independent bound `(11)`, and comparing its two terms against a conductor-power source budget yields the necessary polylogarithmic cutoff condition `(17)` plus the fixed-depth specialization `(19)`--`(20)` for the Lichtman empty-vector component.

A targeted prior-art check on 23 September 2026 found the classical ingredients and many applications of the same level-versus-sifting-range balance, but no basis for claiming a new sieve theorem or a general impossibility result. The conclusion here is deliberately method- and source-frame-specific.

## Boundaries and falsification tests

- **This is a certification barrier, not a lower bound on the true replacement error.** The actual upper/lower gap or the interval remainder combination may be smaller than the generic bounds in `(8)`--`(11)`. A proof exploiting such extra cancellation lies outside the obstruction.
- **The `s^{-s/2}` term is the classical fundamental-lemma guarantee.** A sharper theorem for this exact pair-sieve density may improve constants or the decay law and must be re-priced from its own level dependence.
- **Absolute interval remainders are load-bearing.** Equation `(10)` is intentionally phase-blind. Cancellation among the `r_d`, smoothing that proves a smaller collective discrepancy, or a bilinear treatment coupling them to `K_h` would be genuinely new structure rather than a contradiction of this finding.
- **Polylogarithmic cutoff is necessary here, not sufficient.** When `z` satisfies `(18)`, the remaining level, envelope, endpoint, source-depth and outer-normalization costs still have to be checked.
- **The fixed-`epsilon` specialization matters.** Equation `(20)` assumes the sieve decomposition parameter `epsilon` is fixed as in the cited construction. Letting it shrink with `p` changes the number of components and all constants/support scales and requires a fresh audit; it cannot be inserted silently to manufacture a power gain.
- **Parity-degenerate shifts are excluded exactly as in `MC-472`.** If an active local factor has `nu_h(q)=q`, the pair-sieve survivor set is empty and the nontrivial dimension-two discussion is unnecessary.
- **No claim about the complete-period problem.** On full local periods the endpoint remainder vanishes. The present tariff is specifically the incomplete source-interval transfer needed by the live branch.
- **No Möbius, Mertens, zero-free, or RH consequence follows.** This is a structural and quantitative restriction on one exact-to-surrogate step inside the empty-vector source kernel.

## Consequence for the research line

`MC-481` said that simply centering the Selberg leakage does not create an independent transfer target. The classical two-sided beta-sieve midpoint does: its error is pointwise dominated by an independently countable upper/lower gap. This is the first current surrogate in the empty-vector branch that passes that algebraic independence test.

But the same calculation closes its generic fixed-power-cutoff use. At Lichtman's native `z=Q^epsilon` and level `Q`, the beta-sieve depth is fixed at `1/epsilon`; at a general polynomial cutoff, raising the depth enough for a `p^{-eta}` fundamental-lemma error drives `D=z^s` beyond a polynomial source interval. Therefore this route should be pursued further only if one can place the live cutoff in the polylogarithmic conductor regime **or** exhibit additional cancellation/distribution in the divisor-level remainders before phase-blind absolute closure.

The broader accepted clue remains live. A signed/factorable representation with phase-coupled remainder cancellation, the first-exit boundary channels of `MC-470`, nonempty rough-block components, and pre-positive cross-component interference are not ruled out by `(11)`.