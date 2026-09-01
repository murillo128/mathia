# PC-108 — prime-conductor Hardy remainder converges to a universal Hilbert corner

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-107 shows that the fixed-conductor trace-class remainder `T_n` cannot directly realize the Riemann zero divisor and leaves a singular conductor limit, loss of trace class, or a `det_2`-type construction as a necessary escape. Along prime conductors the first of those escapes can be classified exactly. After the canonical PC-075 residue split, `T_p` converges strongly to one copy of the classical Hilbert matrix supported on the lowest Hardy coordinate. Moreover,

\[
\|T_p\|_{\mathcal S_2}^2=\log p+2\gamma-2+o(1),
\]

and **all of this logarithmically divergent Hilbert--Schmidt mass is carried by that universal finite-Hilbert corner**. After subtracting the corner, the remainder stays Hilbert--Schmidt bounded, tends strongly to zero, and has the exact limiting squared norm

\[
\boxed{\gamma-4+5\log2}.
\]

Consequently no scalar conductor normalization of the canonical prime-shell remainders can converge strongly to a nonzero compact operator, and no scalar normalization can produce a nonzero `S_2` limit. Thus merely letting the prime conductor tend to infinity does cross the uniform trace-class boundary identified by PC-107, but it crosses it through the same classical Hilbert operator already isolated in PC-075, not through a new compact RH spectral object.

No theorem-level historical novelty is claimed for the Hilbert matrix, finite-section convergence, trace ideals, or Ramanujan sums. The durable Prime-Circle content is the exact prime-conductor decomposition and the identification of where the singular conductor mass lives.

## 1. At prime level the full remainder has one explicit two-scale kernel

Use the PC-075 residue decomposition

\[
W_p\Gamma_pW_p^*=-\frac1pC_p\otimes H+T_p,
\]

where the `(r,s)` block of the trace-class remainder is

\[
(T_p)_{rs}
=-\frac{c_p(r+s+1)}p
D_{(r+s+1)/p},
\qquad
D_\alpha:=H_\alpha-H_1.
\]

Put

\[
t=r+s+1,
\qquad 1\le t\le2p-1.
\]

For prime `p`,

\[
c_p(t)=
\begin{cases}
p-1,&p\mid t,\\
-1,&p\nmid t.
\end{cases}
\]

There is only one multiple of `p` in the displayed range, namely `t=p`, and there `D_{t/p}=D_1=0`. Hence the exceptional Ramanujan coefficient multiplies the zero block. The remainder therefore has the exact uniform formula

\[
\boxed{
(T_p)_{rs}=\frac1pD_{t/p}
\qquad(0\le r,s<p).
}
\]

Writing `a,b>=0` for the Hardy indices inside a block gives the entrywise identity

\[
\boxed{
(T_p)_{(r,a),(s,b)}
=
\frac1p
\left(
\frac1{a+b+t/p}-\frac1{a+b+1}
\right).
}
\]

Thus, after primality has removed every interior Ramanujan divisor spike, the conductor dependence is purely the rational mesh `t/p`.

## 2. The lowest Hardy coordinate is exactly a finite Hilbert matrix minus one rank-one mean

Let `e_0` be the lowest Hardy basis vector and let

\[
Q_p=I_{\mathbb C^p}\otimes |e_0\rangle\langle e_0|.
\]

The compression

\[
A_p:=Q_pT_pQ_p
\]

has finite matrix

\[
\begin{aligned}
(A_p)_{rs}
&=\frac1p\left(\frac p{r+s+1}-1\right)\\
&=\boxed{\frac1{r+s+1}-\frac1p}.
\end{aligned}
\]

Let `H^{[p]}` be the `p x p` principal finite section of the classical Hilbert matrix

\[
H=(1/(r+s+1))_{r,s\ge0},
\]

and put

\[
u_p=p^{-1/2}(1,\ldots,1)^T.
\]

Then exactly

\[
\boxed{A_p=H^{[p]}-u_pu_p^*.}
\]

This is already a strong warning for the singular conductor route: the only block whose Hilbert--Schmidt mass can diverge without the extra `1/p` suppression is a completely classical finite Hilbert section with a universal rank-one subtraction.

## 3. In the canonical common embedding, the prime-conductor strong limit is the Hilbert matrix

Embed `\mathbb C^p` as the first `p` coordinates of `\ell^2(\mathbb Z_{\ge0})`, and therefore embed the residue-split remainder in the fixed space

\[
\mathcal K
=\ell^2(\mathbb Z_{\ge0})_{\rm residue}
\otimes
\ell^2(\mathbb Z_{\ge0})_{\rm Hardy}.
\]

Let `P_p` denote the coordinate projection onto the first `p` residue coordinates. Then

\[
H^{[p]}=P_pHP_p
\]

under zero extension. Since `P_p -> I` strongly and `H` is bounded,

\[
P_pHP_p\longrightarrow H
\]

strongly. Also `u_p -> 0` weakly. Indeed, for every `x in \ell^2`, the normalized partial sums

\[
\frac1{\sqrt p}\sum_{r<p}x_r
\]

converge to zero by first truncating `x` and then using Cauchy--Schwarz on the tail. Hence

\[
u_pu_p^*\longrightarrow0
\]

strongly, and therefore

\[
\boxed{A_p\longrightarrow H}
\]

strongly on the residue factor.

Now define

\[
R_p:=T_p-A_p,
\]

where `A_p` is extended by zero off the `a=b=0` Hardy corner. Every matrix entry of `R_p` has `m=a+b>=1`. With `\alpha=t/p in (0,2)`,

\[
\left|
\frac1p\left(
\frac1{m+\alpha}-\frac1{m+1}
\right)
\right|
=
\frac{|1-\alpha|}{p(m+\alpha)(m+1)}
\le
\boxed{\frac1{p\,m(m+1)}}.
\]

For any fixed input basis vector `(s,b)`, summing this square over the `p` residue outputs and over all Hardy outputs gives

\[
\|R_pe_{s,b}\|^2
\le
\frac1p
\sum_{a:\,a+b\ge1}
\frac1{(a+b)^2(a+b+1)^2}
\longrightarrow0.
\]

The family `R_p` is uniformly bounded: PC-079 gives `\Gamma_p=(\mathfrak D_p-I)\Gamma_1` with `\|\Gamma_1\|=\pi` and `\|\mathfrak D_p\Gamma_1\|=\pi`, while the PC-075 reference core has norm `\pi`; hence

\[
\|T_p\|\le3\pi,
\]

and `\|A_p\|\le\pi+1`. Convergence on the dense finite-support vectors therefore extends to strong convergence on all of `\mathcal K`:

\[
\boxed{R_p\longrightarrow0\quad\text{strongly}.}
\]

Combining the two pieces yields the exact conductor-limit classification

\[
\boxed{
T_p
\xrightarrow[p\to\infty,\ p\ {m prime}]{\rm strong}
H\otimes|e_0\rangle\langle e_0|.
}
\]

The limit is the classical noncompact Hilbert operator, with spectrum `[0,\pi]`, not a compact operator with a discrete zero-like spectrum.

## 4. The entire logarithmic `S_2` blowup lies in the universal corner

PC-077 gives, for prime `p`,

\[
\boxed{
\|T_p\|_{\mathcal S_2}^2
=2H_p-2-\log p,
}
\]

where from now on `H_p=\sum_{k=1}^p1/k` denotes the harmonic number rather than the Hilbert operator. Hence

\[
\boxed{
\|T_p\|_{\mathcal S_2}^2
=\log p+2\gamma-2+o(1).
}
\]

The finite corner has the exact Frobenius norm

\[
\|A_p\|_{\mathcal S_2}^2
=
\sum_{r,s=0}^{p-1}
\left(\frac1{r+s+1}-\frac1p\right)^2.
\]

Write

\[
H_p^{(2)}=\sum_{k=1}^p\frac1{k^2},
\qquad
\Delta_1=H_{2p-1}-H_p,
\qquad
\Delta_2=H_{2p-1}^{(2)}-H_p^{(2)}.
\]

Grouping the pairs `(r,s)` by `t=r+s+1`, whose multiplicity is `\min(t,2p-t)`, gives

\[
\boxed{
\|A_p\|_{\mathcal S_2}^2
=
H_p+1-\frac2p+2p\Delta_2-5\Delta_1.
}
\]

The supports of `A_p` and `R_p` are disjoint in the matrix-entry Hilbert--Schmidt inner product, so

\[
\|T_p\|_2^2=\|A_p\|_2^2+\|R_p\|_2^2.
\]

Therefore

\[
\boxed{
\|R_p\|_{\mathcal S_2}^2
=
H_p-3+\frac2p-\log p
-2p\Delta_2+5\Delta_1.
}
\]

Using

\[
H_p-\log p\to\gamma,
\qquad
\Delta_1\to\log2,
\qquad
2p\Delta_2\to1,
\]

we obtain the finite positive limit

\[
\boxed{
\|R_p\|_{\mathcal S_2}^2
\longrightarrow
\gamma-4+5\log2
=0.0429515677\ldots .
}
\]

Thus

\[
\boxed{
\|A_p\|_2^2=\log p+O(1),
\qquad
\|R_p\|_2^2=O(1).
}
\]

The loss of uniform Hilbert--Schmidt control at prime conductor is not hidden arithmetic in the trace-class remainder: its divergent part is exactly the universal finite-Hilbert corner that converges strongly to the classical Hilbert operator.

## 5. No scalar conductor normalization produces a nonzero compact limit

The previous sections give a useful trichotomy for any scalar normalization `a_pT_p` in the same canonical residue embedding.

If `a_p -> a != 0`, then

\[
a_pT_p\longrightarrow aH\otimes|e_0\rangle\langle e_0|
\]

strongly, and the limit is noncompact. If `a_p -> 0`, the uniform operator bound gives

\[
a_pT_p\longrightarrow0
\]

in operator norm. If `|a_p| -> infinity`, the strong convergence of `T_p` to a nonzero Hilbert operator makes `a_pT_p` unbounded on any fixed vector on which the Hilbert limit is nonzero. Passing to subsequences covers every scalar sequence that could have a bounded strong limit. Hence

\[
\boxed{
\text{no scalar normalization of }T_p
\text{ has a nonzero compact strong limit.}
}
\]

The `S_2` threshold is sharper. Since

\[
\|T_p\|_2\sim\sqrt{\log p},
\]

boundedness of `\|a_pT_p\|_2` requires

\[
|a_p|=O((\log p)^{-1/2}),
\]

so `a_p -> 0` and therefore `\|a_pT_p\| ->0`. If the normalized `S_2` mass tends to a positive number, an `S_2`-convergent subsequence is impossible: any `S_2` limit would also be the operator-norm limit, hence zero, contradicting convergence of the `S_2` norms. If the normalized `S_2` mass tends to zero, the limit is the trivial zero operator. Thus

\[
\boxed{
\text{no scalar normalization of }T_p
\text{ produces a nonzero }\mathcal S_2\text{ limit.}
}
\]

This is exactly the natural operator topology needed for the standard continuity theory of the regularized determinant `det_2`. It does not prove that no sequence of scalar-valued regularized determinants can ever have a separately engineered limit; it proves that such a limit cannot come from convergence of the geometry-forced prime-shell operators after scalar conductor normalization.

## 6. Consequence for the PC-107 conductor-limit escape

PC-107 correctly identifies loss of trace class as a necessary escape from the nuclear zero-density obstruction. The prime sequence does lose every uniform trace-ideal bound strong enough to keep the same ordinary Fredholm architecture: already

\[
\|T_p\|_2^2\sim\log p.
\]

But the present calculation shows **why**. The singular mass is the finite-section approximation to the same Hilbert operator that formed the universal absolutely continuous core in PC-075. The conductor limit therefore does not turn the trace-class relative remainder into a compact Hilbert--Polya candidate. Instead it returns to

\[
\boxed{
\text{prime conductor growth}
\to
\text{universal Hilbert boundary layer}
\to
[0,\pi]\text{ continuous spectrum}.
}
\]

Subtracting that universal corner leaves `R_p`, which is uniformly Hilbert--Schmidt and strongly tends to zero, but does **not** converge in `S_2`: its squared `S_2` norm tends to the nonzero constant `\gamma-4+5\log2`. Thus the residual mass escapes through the changing conductor coordinates rather than converging to a fixed compact operator in the canonical refinement embedding.

A surviving Hardy determinant mechanism must therefore use substantially more than `p -> infinity` plus a scalar rescaling of `T_p`: for example a geometry-forced non-scalar recentering/microlocal limit of the escaping remainder, a genuine cross-level operator formed before the PC-075 residue split, or another non-finite construction. Those are open boundaries, not positive evidence.

## 7. Prior-art and novelty audit

Every general analytic ingredient is classical and already anchored in `research/prime_circle/SOURCES.md`.

- The prime Ramanujan-sum formula and its divisor interpretation are standard classical arithmetic.
- Magnus and Rosenblum give the classical Hilbert-matrix spectrum and spectral representation used in PC-075; the strong convergence of principal compressions `P_pHP_p -> H` is a standard consequence of boundedness of `H` and `P_p -> I` strongly.
- Simon's trace-ideal/Fredholm framework, already used in PC-107, supplies the standard `S_2`/regularized-determinant context. The only determinant conclusion used here is the conservative one: `S_2` convergence is the canonical sufficient operator topology for `det_2` continuity, and the prime-shell family admits no nonzero scalar-normalized `S_2` limit.

The exact identity

\[
Q_pT_pQ_p=H^{[p]}-u_pu_p^*
\]

and the residual constant `\gamma-4+5\log2` are consequences of the specific PC-075/PC-077 Prime-Circle remainder. Directed comparison against the Hilbert/Hankel and trace-ideal literature gives no reason to interpret them as a historically new operator theorem; the relevant research value is internal and negative: the most obvious singular prime-conductor continuation of PC-107 is another universality collapse to classical Hilbert data.

This also passes the line's main novelty controls. No zeta function or spectral parameter has been inserted, no arbitrary interpolation is used, and the obstruction is visible before any Mellin/Dirichlet aggregation. The surviving limit is a standard operator already identified independently in PC-075 rather than a rebranded zeta identity.

## 8. Falsification surface and remaining scope

The result has direct failure points.

1. At prime level the exceptional Ramanujan coefficient occurs only at `t=p`, and the corresponding generalized-Hilbert difference must be exactly `D_1=0`; otherwise the uniform block formula fails.
2. Compressing the exact block formula to `a=b=0` must give `1/(r+s+1)-1/p` with no missing sign or scale.
3. For `a+b>=1`, the displayed `1/[p m(m+1)]` bound must hold uniformly for `0<t/p<2`; this is what makes the non-corner part strongly vanish.
4. The PC-077 prime formula must equal `2H_p-2-log p`, and direct multiplicity grouping of the finite Hilbert corner must give the displayed `\Delta_1,\Delta_2` identity.
5. The elementary limits `\Delta_1 -> log2` and `2p\Delta_2 ->1` must hold; failure changes the residual constant.

The conclusion is deliberately limited to the **canonical single-shell Hardy remainder along prime conductors in the canonical residue embedding, with scalar conductor normalization**. It does not rule out squarefree mixed-prime limits with divisor spikes, cross-level Hardy operators, non-scalar conductor-dependent recenterings forced by geometry, nonlinear shell couplings, the cotangent old/new branch, or the global nonlinear uniformization/monodromy branch rooted in PC-017.

## Research consequence

The first singular-conductor escape left by PC-107 has a sharp prime-level answer:

\[
\boxed{
T_p\ \longrightarrow\ H\otimes|e_0\rangle\langle e_0|
\quad\text{strongly},
}
\]

while its logarithmically diverging `S_2` mass is exactly the universal finite-Hilbert boundary layer and its residual `S_2` mass escapes without forming a compact limit. Therefore increasing the prime conductor does not by itself convert the Prime-Circle Hardy remainder into a new discrete RH spectral object; it returns to the classical Hilbert universality class already exposed at fixed conductor.