# MC-189 — Function-field Möbius variance separates exact zero-mode annihilation from transverse equidistribution

**Status:** `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `PROVED-ANALOGUE`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The proved function-field analogue of Möbius short-interval variance in Keating--Rudnick (`MC-S44`) does **not** obtain random-scale local variance by forcing the principal/global Möbius mode to inherit cancellation from the nonprincipal character modes. It has two mathematically separate ingredients:

1. the global degree-`n` Möbius mode vanishes exactly for every `n>=2`; and
2. after the principal character has been removed, Katz equidistribution controls the transverse character family and yields short-interval variance asymptotic to the interval size.

This separation is directly relevant to the integer rough-Möbius frontier of `MC-185`--`MC-188`. The function-field theorem is therefore **not evidence that sufficiently strong transverse equidistribution should by itself control the missing integer rough zero mode**. In the proved analogue, the zero mode is already annihilated independently before the unitary-equidistribution step does its work.

More precisely, over `F_q[t]` let `M_n` denote the monic polynomials of degree `n` and let `mu_q` be the polynomial Möbius function. The zeta function of the affine line is

\[
Z_q(u)=\sum_{f\ {m monic}}u^{\deg f}=\frac1{1-qu}.
\tag{1}
\]

Euler inversion therefore gives the exact generating function

\[
\sum_{f\ {m monic}}\mu_q(f)u^{\deg f}
=\frac1{Z_q(u)}
=1-qu.
\tag{2}
\]

Comparing coefficients,

\[
\boxed{
\sum_{f\in M_n}\mu_q(f)=0
\qquad(n\ge2).
}
\tag{3}
\]

Thus the degree-shell analogue of the global Mertens mode is not merely small: it is identically zero.

For a short interval

\[
I(A;h)=\{f:\|f-A\|\le q^h\},
\qquad
H=q^{h+1},
\]

write

\[
N_\mu(A;h)=\sum_{f\in I(A;h)}\mu_q(f).
\tag{4}
\]

Because the intervals of fixed degree are translates of a common `H`-element low-degree block, averaging `(4)` over all `A\in M_n` multiplies the full degree-`n` sum by a constant incidence factor. Hence `(3)` gives the exact mean

\[
\boxed{
\frac1{q^n}\sum_{A\in M_n}N_\mu(A;h)=0
\qquad(n\ge2).
}
\tag{5}
\]

Keating--Rudnick then prove, for fixed `n`, odd `q->infinity`, and `0<=h<=n-5`,

\[
\boxed{
\frac1{q^n}\sum_{A\in M_n}|N_\mu(A;h)|^2
\sim H.
}
\tag{6}
\]

The proof makes the mode separation explicit. After identifying short intervals with arithmetic progressions modulo `t^{n-h}`, their variance formula is a sum over **nontrivial even characters**:

\[
\operatorname{Var}N_\mu(\cdot;h)
=
\frac1{q^{2(n-h-1)}}
\sum_{\substack{\chi\ ({\rm mod}\ t^{n-h})\\
\chi\ne\chi_0\ {\rm even}}}
|M(n;\mu\chi)-M(n-1;\mu\chi)|^2.
\tag{7}
\]

For primitive even characters the twisted Möbius generating function is `1/L(u,chi)`, and the dominant contribution becomes

\[
\operatorname{Var}N_\mu(\cdot;h)
=
\frac{q^{h+1}}{\Phi_{\rm ev}(t^{n-h})}
\sum_{\substack{\chi\ ({\rm mod}\ t^{n-h})\\
\chi\ {\rm even\ primitive}}}
|\operatorname{tr}\operatorname{Sym}^n\Theta_\chi|^2
+O_n(q^h).
\tag{8}
\]

Katz equidistribution of the Frobenius conjugacy classes then turns the normalized character average into

\[
\int_{U(n-h-2)}
|\operatorname{tr}\operatorname{Sym}^n U|^2\,dU.
\tag{9}
\]

Since `Sym^n` is irreducible, Schur orthogonality makes `(9)` equal to `1`, yielding `(6)`.

The key structural point is therefore exact:

\[
\boxed{
\text{principal mode: }(2)\Rightarrow(3)\Rightarrow(5),
\qquad
\text{transverse modes: }(7)\Rightarrow(8)\Rightarrow(9)\Rightarrow(6).
}
\tag{10}
\]

The second chain does not prove the first.

## 1. Why the principal mode is genuinely independent

Equation `(2)` is an exceptional genus-zero algebraic simplification. The reciprocal zeta function is the degree-one polynomial `1-qu`, so every Möbius coefficient beyond degree one vanishes exactly. No equidistribution theorem, random-matrix integral, short-interval estimate, or averaging over nontrivial characters is needed for `(3)`.

This matters because the variance argument has already centered away the trivial character before Katz equidistribution enters. Equation `(7)` explicitly excludes `chi_0`. The matrix integral therefore measures fluctuations in the character directions transverse to the mean; it cannot contain hidden information about a principal coefficient that has been removed from the sum.

The function-field theorem consequently has a two-input architecture:

\[
\text{exact global cancellation}
\quad+\quad
\text{transverse Frobenius equidistribution}
\quad\Longrightarrow\quad
\text{mean-zero random-scale local variance}.
\tag{11}
\]

Only the second input is supplied by the unitary-monodromy mechanism.

## 2. Comparison with the current logarithmically rough integer block

For the integer line, `MC-180` isolates

\[
g_y(n)=\mu(n)\mathbf1_{P^-(n)>y},
\qquad y=c\log X,
\]

and shows that fixed-power local variance for `g_y` transfers to full Möbius variance with only subpower loss. `MC-185` then proves that centered control is insufficient: the omitted constant mode is a macroscopic increment of

\[
G_y(X)=\sum_{n\le X}g_y(n),
\]

and the live variance target forces a fixed-power estimate for that increment.

`MC-188` supplies the closest integer character-space comparison currently available. At the primorial modulus `q_y=prod_{p<=y}p`, strong smooth-modulus dispersion gives genuine signed control of the reduced-residue-class vector, but the principal character coefficient is exactly the rough global mass `G_y(X)`. When the distinguished character is principal, the theorem subtracts that coefficient; in the nonprincipal branch the available transfer to it is only logarithmic. Thus the integer obstruction is precisely at the mode that the function-field analogue happens to annihilate algebraically.

The comparison should therefore be made as

\[
\begin{array}{c|c|c}
& \text{principal/global mode} & \text{transverse modes}\\
\hline
\mathbb F_q[t] & \text{exactly zero for degree }n\ge2 & \text{Katz/unitary equidistribution}\\
\mathbb Z\text{ rough block} & G_y\text{ only subpower-known} & \text{strong dispersion available}
\end{array}
\tag{12}
\]

The analogy breaks exactly where the live Mathia frontier says it should.

## 3. What the proved analogue does and does not suggest

The function-field result remains highly informative. It demonstrates that a genuine arithmetic character family plus Frobenius monodromy can produce the square-root-fluctuation scale for Möbius short intervals, rather than merely a logarithmic saving. But the theorem achieves this **after** the principal mode is solved by `(2)`.

Accordingly, importing only the transverse half of the analogy into the integer problem cannot repair `MC-188`. A number-field analogue of Katz equidistribution, a stronger family variance theorem, or a more random-matrix-like description of nonprincipal twists would still leave the principal rough coefficient untouched unless the proposed mechanism supplies one of the following additional structures:

- an independent arithmetic annihilator or fixed-power estimate for the principal rough mode;
- a theorem in which the principal coefficient is not projected out but is quantitatively coupled to the controlled nonprincipal family; or
- a different statistic whose positivity or conservation law contains both mean and transverse energy without requiring the missing mean as an external input.

This is a sharper requirement than the generic statement that "more equidistribution is needed." The proved analogue shows that **equidistribution and zero-mode control are logically distinct resources even in the setting where the desired variance theorem is known exactly**.

## 4. Prior art and novelty audit

The mathematical inputs are established prior art. `MC-S44` is Jonathan P. Keating and Zeev Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, Algebra & Number Theory 10 (2016), 375--420, DOI `10.2140/ant.2016.10.375`. Their equation (1.5) records the exact full degree-shell Möbius sum, Theorem 1.2 / Theorem 7.1 gives `(6)`, equation (7.5) gives the nontrivial-character variance decomposition, and equations (7.14)--(7.16) give the Frobenius/unitary evaluation. No novelty is claimed for any of these results.

A targeted literature check found the same theorem and its character/Frobenius mechanism, together with later function-field work using short-interval/Hayes characters and Frobenius equidistribution, but no basis for claiming that the decomposition `(10)` is a new theorem. The Mathia contribution is the **frontier comparison** with `MC-185`--`MC-188`: the strongest proved analogue currently in the line separates rather than bridges principal and transverse cancellation, and its principal side is solved by a special algebraic identity absent from the integer rough problem.

## 5. Boundaries and falsification tests

- The result is a structural comparison, not a transfer theorem from `F_q[t]` to the integers.
- The limit in Keating--Rudnick is `q->infinity` with degree parameters fixed. It must not be read as an integer asymptotic with `X->infinity`.
- The modulus `t^{n-h}` in the function-field short-interval character decomposition is not the integer primorial modulus of `MC-188`; `(12)` compares the principal/transverse **role**, not identical arithmetic objects.
- The exact cancellation `(3)` uses the genus-zero zeta function of `F_q[t]`. Higher-genus function fields need not have the same degree-one reciprocal-zeta collapse, so the statement is not a universal function-field principle.
- Equation `(6)` is an averaged short-interval variance theorem. It does not give a uniform bound for every interval and does not by itself imply an integer Mertens estimate.
- A future integer theorem that genuinely couples principal and nonprincipal modes would not be ruled out. It would contain structure absent from the Keating--Rudnick variance step and would be exactly the kind of new ingredient requested by `MC-188`.

The comparison is falsified if the function-field variance proof requires Katz equidistribution to establish the global mean `(5)`, or if the principal character survives inside the character average that becomes `(9)`. The source formulas show the opposite: the global degree-shell cancellation comes from `1/Z_q(u)=1-qu`, while the variance sum explicitly excludes the principal character.

## Consequence for the live frontier

The function-field analogy should no longer be used as evidence that a sufficiently strong theorem about transverse characters will automatically force the rough integer zero mode. In the proved model, **the principal mode is paid for separately and exactly**.

This sharpens the next search after `MC-188`: either find a source-side arithmetic mechanism that independently upgrades `G_y` from Korobov--Vinogradov/subpower cancellation to a fixed power, or find a genuinely new coupling in which the principal rough coefficient participates in the same controlled object as the transverse modes. Stronger nonprincipal equidistribution alone is not the missing bridge.