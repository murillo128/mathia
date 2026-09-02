# PC-130 — coprime Hessian CRT incidence is fixed Dirichlet-L(2) data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `PRIOR-ART-REDIRECTION` + `NEGATIVE` for treating the coprime CRT incidence left open by PC-129 as a new finite arithmetic alphabet or an unexplained finite spectral carrier. This does not classify the nonlinear singular/eigenvalue problem of the resulting finite matrices, cross-level compositions, noncoprime shell pairs, infinite-level limits, or the global uniformization/monodromy branch of PC-017.

PC-129 showed that for coprime shell indices `(m,n)=1`, the inverse-square conductance multiset of the PC-128 bipartite Hessian is exactly the common-anchor inverse-square profile on the product shell `P_{mn}^*`; the only finite information not already visible in that multiset was how CRT attaches each product-shell weight to an `m`-vertex and an `n`-vertex.

That remaining incidence has an exact harmonic classification. After independent multiplicative Fourier transforms on the two endpoint groups, the whole rectangular conductance matrix is just a two-dimensional reshaping of the one-dimensional multiplicative transform of the product-shell anchor profile. Every transformed matrix entry is an explicit unit phase times a fixed Dirichlet value `L(2,eta)`, and the pair of endpoint characters runs bijectively over all characters modulo `mn`.

Thus the coprime CRT incidence is real relational information in the vertex basis, but it introduces no new finite coefficient arithmetic beyond the classical fixed-critical-value package already encountered in the pointed inverse-square branch. The unresolved part is nonlinear use of the **arrangement** of those fixed values, not a hidden new local or Fourier coefficient.

## 1. The coprime conductance matrix is a CRT reshape of one anchor profile

Let

\[
(m,n)=1,
\qquad
N=mn,
\qquad
G_q=(\mathbb Z/q\mathbb Z)^\times,
\]

and put

\[
r=\varphi(m),
\qquad
s=\varphi(n).
\]

Write the primitive shell vertices as

\[
\alpha_a=\zeta_m^a=\zeta_N^{na},
\qquad a\in G_m,
\]

and

\[
\beta_b=\zeta_n^b=\zeta_N^{mb},
\qquad b\in G_n.
\]

The off-diagonal conductance block of the PC-128 Hessian is

\[
C_{m,n}(a,b)
:=\frac1{|\alpha_a-\beta_b|^2}.
\]

Define the product-shell pointed profile

\[
w_N(u)
:=\frac1{|1-\zeta_N^u|^2}
=\frac1{4\sin^2(\pi u/N)},
\qquad u\in G_N.
\]

Then

\[
\boxed{
C_{m,n}(a,b)=w_N(na-mb).
}
\]

Because `(m,n)=1`, the map

\[
\boxed{
G_m\times G_n\longrightarrow G_N,
\qquad
(a,b)\longmapsto u=na-mb
}
\]

is a bijection. Its inverse is

\[
a\equiv n^{-1}u\pmod m,
\qquad
b\equiv -m^{-1}u\pmod n.
\]

This recovers the edge-set statement of PC-129 but also fixes the exact rectangular reshaping that carries the CRT incidence.

## 2. Two-sided multiplicative Fourier transform

For characters `chi` of `G_m` and `psi` of `G_n`, use the normalized character bases

\[
e_\chi(a)=\frac{\chi(a)}{\sqrt r},
\qquad
f_\psi(b)=\frac{\psi(b)}{\sqrt s}.
\]

Let

\[
M_{\chi,\psi}
:=\langle e_\chi,C_{m,n}f_\psi\rangle
=\frac1{\sqrt{rs}}
\sum_{a\in G_m}\sum_{b\in G_n}
\overline{\chi(a)}\,C_{m,n}(a,b)\,\psi(b).
\]

Under the CRT change of variables from Section 1, define

\[
\eta_{\chi,\psi}(u)
:=\overline{\chi(u\bmod m)}\,\psi(u\bmod n),
\qquad u\in G_N,
\]

and the unit phase

\[
\gamma_{\chi,\psi}
:=\overline{\chi(n^{-1}\bmod m)}\,
\psi(-m^{-1}\bmod n).
\]

Then exactly

\[
\boxed{
M_{\chi,\psi}
=
\frac{\gamma_{\chi,\psi}}{\sqrt{rs}}
\sum_{u\in G_N}\eta_{\chi,\psi}(u)w_N(u).
}
\]

The phase is separable into a row phase depending only on `chi` and a column phase depending only on `psi`; it can therefore be removed by diagonal unitaries and cannot create singular-value information.

More importantly, CRT gives

\[
\widehat{G_N}\cong\widehat{G_m}\times\widehat{G_n}.
\]

Complex conjugation on the first factor is a bijection, so

\[
\boxed{
(\chi,\psi)\longmapsto\eta_{\chi,\psi}
}
\]

runs bijectively over **every** Dirichlet character modulo `N` viewed as a character of `G_N`. Thus the `r s=phi(N)` entries of the two-dimensional Fourier table `M` are, up to the separable phases and common normalization, precisely the one-dimensional character coefficients of the single pointed profile `w_N`, each occurring once.

This is stronger than equality of the conductance multiset: the entire CRT incidence matrix is Fourier-equivalent to a canonical reshape of the product-shell anchor transform.

## 3. Every transformed entry is a fixed `L(2,eta)` value

The Mittag-Leffler expansion gives, for every `u in G_N`,

\[
w_N(u)
=
\frac{N^2}{4\pi^2}
\sum_{k\in\mathbb Z}\frac1{(u+kN)^2}.
\]

Let `eta` be any Dirichlet character modulo `N`, primitive or imprimitive, extended by zero away from `G_N`. Absolute convergence permits exchanging the finite character sum with the Mittag-Leffler series:

\[
\begin{aligned}
S_N(\eta)
&:=\sum_{u\in G_N}\eta(u)w_N(u)\\
&=\frac{N^2}{4\pi^2}
\sum_{\substack{q\in\mathbb Z\\q\ne0}}
\frac{\eta(q)}{q^2}\\
&=\boxed{
\frac{N^2}{4\pi^2}
\bigl(1+\eta(-1)\bigr)L(2,\eta)
}.
\end{aligned}
\]

Therefore the complete coprime conductance table in multiplicative Fourier coordinates is

\[
\boxed{
M_{\chi,\psi}
=
\frac{N^2}{4\pi^2\sqrt{rs}}
\gamma_{\chi,\psi}
\bigl(1+\eta_{\chi,\psi}(-1)\bigr)
L(2,\eta_{\chi,\psi}).
}
\]

In particular,

\[
\boxed{
\eta_{\chi,\psi}(-1)=-1
\Longrightarrow
M_{\chi,\psi}=0.
}
\]

So endpoint characters of opposite parity do not couple. For matching parity,

\[
\boxed{
M_{\chi,\psi}
=
\frac{N^2}{2\pi^2\sqrt{rs}}
\gamma_{\chi,\psi}
L(2,\eta_{\chi,\psi}).
}
\]

The principal-principal entry is the standard reduced-residue cosecant sum:

\[
\boxed{
M_{1,1}
=
\frac{J_2(N)}{12\sqrt{rs}},
\qquad
J_2(N)=N^2\prod_{p\mid N}(1-p^{-2}).
}
\]

PC-035 derived the same `csc^2 -> L(2,chi)` mechanism for a prime pointed shell. Here the same classical transform is needed at the composite product modulus `N=mn`, and CRT shows that it classifies **all** Fourier coefficients of the coprime cross-shell incidence matrix, not merely a standalone anchor vector.

For even characters these fixed positive-critical values can equivalently be expressed, after passage to the primitive ancestor and its missing Euler factors, in the standard Gauss/generalized-Bernoulli algebraic package. No free complex spectral parameter has appeared.

## 4. The diagonal blocks of the full Hessian add no independent coefficient data

The PC-128 bipartite Hessian is the weighted Laplacian

\[
L_{m,n}
=
\begin{pmatrix}
D_A&-C_{m,n}\\
-C_{m,n}^T&D_B
\end{pmatrix},
\qquad
D_A=\operatorname{diag}(C_{m,n}\mathbf1),
\quad
D_B=\operatorname{diag}(C_{m,n}^T\mathbf1).
\]

The degree profiles are only row and column marginals of `C_{m,n}`. Their multiplicative Fourier coefficients are therefore principal slices of the same table `M`. With the normalized conventions above,

\[
\widehat d_A(\chi)=\sqrt{s}\,M_{\chi,1},
\qquad
\widehat d_B(\psi)=\sqrt{r}\,M_{1,\overline\psi}.
\]

Consequently, after the block unitary change of basis by characters, the diagonal multiplication blocks are convolution matrices whose entries are again principal slices of `M`. Explicitly,

\[
\boxed{
(\widetilde D_A)_{\chi,\chi'}
=
\sqrt{\frac{s}{r}}\,
M_{\chi\overline{\chi'},1},
}
\]

and

\[
\boxed{
(\widetilde D_B)_{\psi,\psi'}
=
\sqrt{\frac{r}{s}}\,
M_{1,\overline\psi\psi'}.
}
\]

Thus every finite matrix coefficient of the full coprime Hessian in the multiplicative character basis is drawn from the same fixed `L(2,eta)` table. The degree terms do not introduce a second arithmetic family hidden from the off-diagonal conductances.

This statement is about the **coefficient algebra**, not a diagonalization theorem. In general `M` is rectangular and not diagonal, and the convolutional diagonal blocks need not commute with the off-diagonal block. Their eigenvalues and singular values can therefore be nontrivial nonlinear combinations of the fixed special values.

## 5. Exact control: `(m,n)=(3,4)`

PC-129 gives

\[
C_{3,4}
=
\begin{pmatrix}
2+\sqrt3&2-\sqrt3\\
2-\sqrt3&2+\sqrt3
\end{pmatrix}.
\]

Both endpoint unit groups are of order two. Ordering their characters as principal and sign, the normalized two-sided multiplicative Fourier transform is

\[
\boxed{
M=
\begin{pmatrix}
4&0\\
0&2\sqrt3
\end{pmatrix}.
}
\]

Here `N=12`. The principal character gives

\[
\frac{J_2(12)}{12\sqrt{4}}
=
\frac{96}{24}=4,
\]

while the two parity-mismatched product characters vanish exactly. The remaining even product character gives `2 sqrt(3)` from the displayed `L(2,eta)` formula. This reproduces the full matrix without fitting and checks the normalization, CRT sign, and parity factor simultaneously.

A second numerical audit at `(m,n)=(5,3)`, including complex order-four characters on `G_5`, verifies the phase formula and the CRT change of variables to machine precision; it is not used as evidence for the exact derivation.

## 6. Prior art and novelty audit

No theorem-level novelty is claimed for the harmonic identities.

- The Mittag-Leffler expansion of `csc^2` and the resulting Dirichlet-character special-value formulas are classical. PC-035 already uses the prime-modulus specialization.
- Beck--Halloran, already anchored in `research/prime_circle/SOURCES.md`, treats finite trigonometric sums weighted by Dirichlet characters through discrete Fourier analysis and places such sums inside an established class-number/character framework.
- Liu--Xin gives a current systematic treatment of root-of-unity-weighted trigonometric power sums, including even cosecant powers.
- Gao--Guo gives a current spectral/determinantal treatment of trigonometric matrices in terms of Dirichlet `L`-values and Gauss sums, reinforcing the novelty boundary for interpreting a finite trigonometric character matrix as a new `L`-mechanism.
- The dual CRT factorization of finite abelian unit groups and their character groups is standard finite harmonic analysis.

Directed searches for bipartite roots-of-unity inverse-square matrices, cosecant-squared character matrices, and trigonometric determinants with Dirichlet characters did not locate this exact PC-128/129 coprime-shell reshaping formula. That absence is not evidence of historical priority. The durable prime-circle contribution is the **scope classification**: the specific relational datum left open by PC-129 becomes exactly the already-classical product-shell `L(2)` character table after the harmonic transform forced by CRT.

This finding is distinct from PC-044. PC-044 studies a **single-level primitive compression** of the full regular-polygon inverse-square Laplacian and obtains a finite Dirichlet--Bernoulli coupling matrix after deleted nonprimitive vertices are accounted for. PC-130 instead studies the **cross-shell coprime bipartite Hessian** of PC-128/129 and resolves its remaining CRT endpoint incidence by a two-sided character transform. The two calculations share the same classical finite-character boundary but classify different operators.

## 7. Research consequence and surviving boundary

PC-129 left one finite question open in the coprime case: perhaps the CRT incidence of the product-shell anchor weights carried a new harmonic arithmetic structure even though the edge multiset itself did not. At the linear coefficient level, that possibility is now closed:

\[
\boxed{
\text{coprime shell Hessian CRT incidence}
\longrightarrow
\text{two-sided multiplicative Fourier table}
\longrightarrow
\{L(2,\eta):\eta\bmod mn\}
}
\]

up to explicit parity, normalization, and separable character phases. Because `(chi,psi) -> eta` is bijective, there is no leftover linear Fourier datum outside that fixed Dirichlet package.

This does **not** prove that the singular values or eigenvalues of the finite Hessian are individually classical `L`-values, nor that nonlinear invariants of their arrangement are trivial. In fact, a nonlinear matrix function can mix many fixed `L(2,eta)` values in a way not captured by any individual character coefficient. Nor does the result address noncoprime pairs, where the resultant prime-power relation changes the shell interaction, or any cross-level/infinite composition that is not a finite transform of one `C_{m,n}`.

The practical boundary is therefore precise: for coprime PC-128 Hessians, **new finite arithmetic cannot be claimed from the raw CRT incidence or its linear character coordinates**. A surviving RH-relevant mechanism would have to exploit a controlled nonlinear/cross-level organization of these matrices, a genuinely new limiting operator with an intrinsic analytic parameter, the noncoprime resultant structure, or the global primitive-only uniformization/monodromy defect of PC-017.

## 8. Exact falsification tests

The classification can be checked without asymptotics or fitting:

1. verify that `(a,b) -> na-mb mod mn` is a bijection `G_m x G_n -> G_mn` for `(m,n)=1`;
2. substitute the CRT inverse residues to recover the phase `gamma_{chi,psi}` and product character `eta_{chi,psi}`;
3. verify that `(chi,psi) -> eta_{chi,psi}` is a bijection of character sets;
4. apply the absolutely convergent Mittag-Leffler expansion and pair positive/negative integers to obtain the factor `1+eta(-1)`;
5. check the principal mode against `J_2(N)/12`;
6. recover the Fourier coefficients of both degree profiles from the principal row/column slices of `M`;
7. for `(3,4)`, recover exactly `diag(4,2 sqrt(3))` in the two-sided character basis;
8. distinguish the claim from a spectral diagonalization: no assertion is made that general singular/eigenvalues of `C_{m,n}` or `L_{m,n}` equal individual Dirichlet special values.

Failure of the CRT bijection, the character phase, the parity factor, or either marginal formula would invalidate the main classification.