# MC-337 — Odd source parity creates an all-or-nothing self-phase barrier

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-336` isolated self-phase leakage at the reciprocal endpoint and proved the exact self-phase-excluded degree theorem for **even** source rank `R`, leaving the odd-`R` quotient unresolved. The odd case is not merely a routine parity variant. The source phases acquire one global relation, and that relation changes the punctured-cube approximation geometry qualitatively.

Assume throughout that `R>=3` is odd. Continue the reciprocal endpoint notation

\[
G=\mathbf F_2^R,
\qquad
\Xi=G\setminus\{0\},
\qquad
s_i=\mathbf1+e_i,
\qquad
x_i(a)=(-1)^{a\cdot s_i}.
\tag{1}
\]

Then

\[
\prod_{i=1}^R x_i(a)=1
\tag{2}
\]

for every `a`, and the source-phase map has kernel

\[
\ker(a\mapsto(x_1(a),\ldots,x_R(a)))
=\{0,\mathbf1\}.
\tag{3}
\]

Its image is therefore the even-parity sign subgroup

\[
H:=\left\{x\in\{\pm1\}^R:\prod_i x_i=1\right\},
\qquad
|H|=:L=2^{R-1}.
\tag{4}
\]

In particular the nonprincipal mode `a=\mathbf1` has **exactly the same source phases** as the principal mode `a=0`.

Impose the same self-phase-excluded source architecture as in `MC-336`: for a prime `r` in source cell `s_i`,

\[
w_{a,r}
=g_r(x_1(a),\ldots,\widehat{x_i(a)},\ldots,x_R(a)),
\qquad
\deg g_r\le d.
\tag{5}
\]

For `0\le d\le R-2`, the normalized endpoint outputs are exactly the span of the nonconstant characters of `H` whose subset/complement class has minimal Hamming weight at most `d+1`. Let

\[
h:=\frac{R-1}{2},
\qquad
A_d:=\sum_{k=1}^{\min(d+1,h)}\binom Rk,
\qquad
q_d:=L-1-A_d.
\tag{6}
\]

Thus `A_d` is the dimension of the reachable character space and `q_d` counts the missing nonconstant characters. Writing `N:=2^R=2L`, the exact best all-nonprincipal dephasing error is

\[
\boxed{
\inf_F\sum_{a\in\Xi}|F(a)-1|^2
=
N\,\frac{L+q_d}{L+q_d+1}
\qquad(0\le d\le R-2),
}
\tag{7}
\]

where the infimum ranges over all outputs realizable by `(5)`.

Consequently

\[
\boxed{
\frac1{N-1}
\inf_F\sum_{a\ne0}|F(a)-1|^2
\ge
\frac{NL}{(N-1)(L+1)}
=1-o(1)
}
\tag{8}
\]

**uniformly for every `d<=R-2`**. Once `d+1>=h`, all nonconstant characters of `H` are already reachable, but the error does not collapse; it enters the plateau

\[
\boxed{
E_d=\frac{NL}{L+1}
\qquad
\left(\frac{R-3}{2}\le d\le R-2\right).
}
\tag{9}
\]

Exact dephasing appears only at the final degree

\[
\boxed{d=R-1.}
\tag{10}
\]

At that point the global parity relation itself reconstructs the forbidden own phase:

\[
g_i(x_{-i})=\prod_{j\ne i}x_j=x_i
\quad\text{on }H,
\tag{11}
\]

so

\[
x_i g_i=\prod_{j=1}^R x_j=1.
\tag{12}
\]

Therefore odd source rank produces an **all-or-nothing locality threshold**. Syntactic self-phase exclusion remains strongly anti-programmable at every submaximal degree, even after the reachable space already contains every nonconstant quotient character; at degree `R-1`, the parity constraint makes own-phase reconstruction exact and the matched filter returns immediately.

No estimate for `M(x)` follows.

## 1. Odd `R` turns source coordinates into an even-parity quotient

Let `M` be the binary `R x R` matrix with columns `s_i`. As in `MC-336`,

\[
M=I+J
\tag{13}
\]

over `\mathbf F_2`, where `J` is the all-ones matrix. If `Mc=0` and `t=\sum_i c_i`, then

\[
c=t\mathbf1.
\tag{14}
\]

For odd `R`, `c=\mathbf1` really lies in the kernel because

\[
M\mathbf1=(R-1)\mathbf1=0
\quad\text{in }\mathbf F_2.
\tag{15}
\]

Hence `rank(M)=R-1` and the kernel is exactly `span{\mathbf1}`. The source-phase map therefore has two-element fibers `{a,a+\mathbf1}`.

Equation `(2)` follows either from this rank calculation or directly from

\[
\sum_{i=1}^R s_i=(R-1)\mathbf1=0.
\tag{16}
\]

The image has size `2^{R-1}` and lies inside the size-`2^{R-1}` group `H`, so it equals `H`.

This already exposes the main difference from even `R`. Removing only the principal mode `a=0` does **not** puncture the source-phase group `H`: the same point `x=(1,\ldots,1)` remains in the objective through its second preimage `a=\mathbf1`.

More precisely, for every function `F:H\to\mathbf C`,

\[
\sum_{a\in\Xi}|F(x(a))-1|^2
=
|F(\mathbf1_H)-1|^2
+2\sum_{x\in H\setminus\{\mathbf1_H\}}|F(x)-1|^2.
\tag{17}
\]

Thus the odd-`R` problem is a **weighted full-group** approximation problem, not the punctured-group problem of the even case.

## 2. Reachable characters are subset classes modulo complement

Characters of `H` are restrictions of cube monomials

\[
x_K:=\prod_{j\in K}x_j,
\qquad K\subseteq[R].
\tag{18}
\]

Because `\prod_jx_j=1` on `H`,

\[
x_K=x_{K^c}
\quad\text{on }H.
\tag{19}
\]

Hence characters are indexed by subset classes

\[
[K]:=\{K,K^c\}.
\tag{20}
\]

Since `R` is odd, each class has a unique representative of size at most

\[
h=(R-1)/2.
\tag{21}
\]

There are therefore

\[
\sum_{k=0}^{h}\binom Rk=2^{R-1}=L
\tag{22}
\]

such character classes.

Now take a coefficient in source cell `i` satisfying `(5)`. Every monomial of `g_r` has the form `x_T` with

\[
i\notin T,
\qquad
|T|\le d.
\]

Multiplication by the source phase produces

\[
x_i x_T=x_{T\cup\{i\}},
\qquad
1\le |T\cup\{i\}|\le d+1.
\tag{23}
\]

Therefore every reachable character class has a representative of size at most `d+1`.

Conversely, let `[K]` be nonconstant and let its unique small representative satisfy

\[
1\le |K|\le\min(d+1,h).
\]

Choose `i\in K` and one endpoint prime from cell `s_i`. Taking

\[
g_r=A\,x_{K\setminus\{i\}}
\tag{24}
\]

and all other coefficients zero realizes `x_K`. Hence the reachable space is exactly the span counted by `A_d` in `(6)`.

For `d<=R-2`, the constant character is absent. Its only subset representatives are `\varnothing` and `[R]`; output monomials in `(23)` are nonempty and have size at most `R-1`.

This produces a second sharp feature. When

\[
d\ge h-1=\frac{R-3}{2},
\tag{25}
\]

every **nonconstant** character of `H` is already available. Increasing the degree further through `R-2` adds no new quotient character at all. The only missing direction is the constant one.

## 3. Exact weighted projection formula

Let `\mathcal A_d` denote the `A_d` reachable nonconstant characters. Under the weighted inner product induced by `(17)`, distinct characters `\chi,\psi\in\mathcal A_d` satisfy

\[
\langle\chi,\psi\rangle_w
=2\sum_{x\in H}\chi(x)\overline{\psi(x)}
-\chi(\mathbf1_H)\overline{\psi(\mathbf1_H)}.
\tag{26}
\]

All characters equal one at the identity and are orthogonal on the uniform finite group `H`, so

\[
\boxed{
G_d=N I_{A_d}-\mathbf1\mathbf1^*.
}
\tag{27}
\]

The weighted inner product of the constant target with every reachable nonconstant character is

\[
\langle1,\chi\rangle_w
=2\sum_{x\in H}\chi(x)-1
=-1,
\tag{28}
\]

while

\[
\|1\|_w^2=N-1.
\tag{29}
\]

Since `A_d<L<N`, the Gram matrix is invertible and

\[
G_d^{-1}
=
\frac1N I
+
\frac1{N(N-A_d)}\mathbf1\mathbf1^*.
\tag{30}
\]

The squared norm of the orthogonal projection of the target onto the reachable space is therefore

\[
\mathbf1^*G_d^{-1}\mathbf1
=
\frac{A_d}{N-A_d}.
\tag{31}
\]

Subtracting from `(29)` gives

\[
E_d
=N-1-\frac{A_d}{N-A_d}
=N\frac{N-A_d-1}{N-A_d}.
\tag{32}
\]

Using

\[
A_d=L-1-q_d
\tag{33}
\]

yields exactly `(7)`:

\[
E_d
=N\frac{L+q_d}{L+q_d+1}.
\tag{34}
\]

Because `q_d>=0`, `(8)` follows immediately. If `(25)` holds then `q_d=0`, giving the plateau `(9)`.

The point is not merely that exact dephasing fails. Even the best least-squares approximation remains asymptotically as bad as the zero output throughout the entire submaximal-degree regime.

## 4. Why the final degree collapses everything

At `d=R-1`, source cell `i` is allowed to use the product of all `R-1` other source phases. The parity relation `(2)` gives

\[
\prod_{j\ne i}x_j=x_i^{-1}=x_i,
\tag{35}
\]

so the apparently self-phase-excluded coefficient in `(11)` reconstructs the own phase exactly.

Multiplication by the endpoint character then gives the constant output `(12)` prime by prime. Thus the constant character enters the reachable space at exactly `d=R-1`, and the dephasing error drops from the plateau `(9)` to zero.

This also sharpens the semantic meaning of **self-phase exclusion**. For odd `R`, merely hiding the variable `x_i` is not information-theoretic exclusion: `x_i` is determined by the other variables. What protects the architecture below maximal degree is the **complexity of reconstruction**. Any future source-natural locality condition must therefore forbid not only literal access to `x_i` but also sufficiently cheap algebraic reconstruction of it from admitted cross-source data.

## 5. Contrast with the even-rank theorem

For even `R`, `MC-336` has independent source coordinates. The principal mode is a genuinely unique source-phase point, so the objective becomes a punctured-cube approximation problem. At `d=R-2`, only the top source monomial remains unavailable and the normalized squared error falls to approximately `1/2` before exact dephasing appears at `R-1`.

For odd `R`, the two-to-one phase map puts a nonprincipal mode back at the identity. The quotient therefore has no free puncture. Even when every nonconstant quotient character is available, their weighted span remains almost orthogonal to the constant target, and the normalized squared error stays at `1-o(1)` until the constant mode itself becomes reachable.

So parity of `R` is a genuine capacity parameter:

\[
\boxed{
\begin{array}{ll}
R\ \text{even}:&\text{near-maximal nonconstant support already gives partial dephasing};\\
R\ \text{odd}:&\text{all nonconstant quotient support still gives asymptotically no dephasing}.
\end{array}
}
\tag{36}
\]

The difference is entirely finite and structural; no analytic number-theory estimate is used.

## 6. Prior art and novelty boundary

The harmonic ingredients are classical. Fourier characters form an orthogonal basis on finite abelian groups, and restriction to a subgroup identifies characters modulo the annihilator. For the Boolean-cube language, Ryan O'Donnell's *Analysis of Boolean Functions* (Cambridge University Press, 2014; DOI `10.1017/CBO9781139814782`; corrected arXiv edition `2105.10386`) is a standard reference for Walsh characters and multilinear Fourier expansions. Standard finite-abelian Fourier/Pontryagin duality likewise identifies the dual of a subgroup as the ambient dual modulo its annihilator; the subset/complement identification `(19)` is exactly this elementary mechanism for the even-parity subgroup.

A targeted literature search on 16 September 2026 located these standard Boolean-Fourier and finite-abelian-group frameworks. No external theorem is needed for `(3)`–`(35)`, and no novelty is claimed for subgroup duality, the complement identification, character orthogonality, or the Gram-matrix calculation. The durable Mathia delta is the **odd-rank specialization of the reciprocal endpoint information-flow model**: it closes the parity case left open by `MC-336` and shows that the same global source relation that ultimately permits own-phase reconstruction also makes every submaximal-degree approximation dramatically worse.

## Boundaries and falsification tests

- **Odd `R>=3` is load-bearing.** The one-dimensional kernel and complement-paired character classes come from the exact relation `sum_i s_i=0`. Even `R` is governed by `MC-336` instead.
- **The objective still includes every nonprincipal mode.** The weighted identity point in `(17)` exists because `a=\mathbf1` is nonprincipal in `G` but source-phase-indistinguishable from `a=0`. Removing that mode would recover a genuinely punctured quotient problem and change `(7)`.
- **Self-phase exclusion is the exact rule from `MC-336`.** Coefficients may depend arbitrarily on the other source variables up to multilinear degree `d`; no norm, rank, or variation restriction is added.
- **Every endpoint source cell must occur for the converse reachability statement.** The reciprocal endpoint has this property. Support containment alone does not need equal multiplicities.
- **The plateau is not an energy statement.** Coefficients may be arbitrarily large. The obstruction comes from the missing constant quotient character.
- **At `d=R-1`, self-phase exclusion becomes reconstructively vacuous.** Equation `(35)` is an explicit algebraic leakage path. Any stronger locality definition must exclude equivalent reconstruction, not merely the variable name.
- **No analytic family estimate is proved.** This is a finite capacity theorem. It does not show that an actual prime-family argument supplies such coefficients or that the restriction improves a bound for `M(x)`.
- **No zero-free information enters.** The proof uses only the reciprocal endpoint frame, finite-group character orthogonality, and exact least squares.
- **No RH implication is claimed.** The finding prices one candidate information-flow architecture; the missing arithmetic step remains external.

## Consequence for the research line

`MC-336` left odd source rank as the last parity ambiguity in the source-coordinate degree model. That ambiguity is now closed exactly.

The combined lesson is sharper than a generic low-degree requirement. A useful analytic coefficient architecture needs a source-local information-flow rule for which **own-phase reconstruction remains expensive in the actual quotient geometry**. In even rank, independence makes exclusion literal. In odd rank, own phase is globally determined by the others, so only a complexity bound prevents reconstruction; the exact threshold is maximal degree `R-1`.

This suggests the next analytic question in a representation-independent form: identify a naturally generated coefficient class for the prime family whose information graph or sigma-algebra makes the local character phase inaccessible except through a quantitatively expensive global reconstruction. Degree, energy, rank, and variation are then secondary budgets on that information-flow restriction rather than substitutes for it.