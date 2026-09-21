# PC-389 — successive primorial boundary transport is Buchstab deletion

**Status:** `EXACT-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the natural inclusion/compression transport between successive primorial boundary windows.

PC-388 identifies a primorial primitive boundary window with the classical rough-number wheel, but leaves cross-level transport as a possible place where non-scalar structure could survive the support-level classicalization. For the most direct transport—keep the same anchored exponent window while passing from a primorial `N_x` to the next primorial `qN_x`—the support change is exactly one Buchstab sieve step. In the whole prime-only mesoscopic regime `H=x^u`, `1<u<2`, this transport deletes exactly one vertex, the next prime `q=p_+(x)`.

For pairwise Hermitian kernel matrices whose entries are the line-forced normalized chord kernel, the corresponding cross-level operator is therefore asymptotically just the principal minor obtained by deleting that one vertex. The residual change of the chord kernel caused by replacing the polygon order `N_x` by `qN_x` is `o(1)` in operator norm on every polynomial boundary window. Hence the simplest successive-level spectral flow has no distributed new carrier in this regime: it is Cauchy interlacing plus a one-vertex deletion already dictated by the classical sieve support.

This does **not** rule out cross-level constructions that mix fibers nonlocally, use a different geometric correspondence, retain growing-depth history, or form a genuinely nonseparable operator before boundary restriction. It sharply closes the canonical same-window inclusion/compression escape left open by PC-388.

## 1. Exact one-prime recursion for the primitive boundary

Let

\[
N_x:=\prod_{p\le x}p,
\qquad
q:=p_+(x)=\min\{p>x:p\text{ prime}\},
\tag{1}
\]

and for `H<N_x` define, as in PC-388,

\[
R_x(H):=\{1\le a\le H:(a,N_x)=1\}.
\tag{2}
\]

After adjoining the next prime, the new primorial is

\[
N_x^+:=qN_x,
\tag{3}
\]

with boundary support

\[
R_x^+(H):=\{1\le a\le H:(a,qN_x)=1\}.
\tag{4}
\]

The deleted set is exact:

\[
\boxed{
R_x(H)\setminus R_x^+(H)
=
q\,R_x(\lfloor H/q\rfloor).
}
\tag{5}
\]

Indeed, an old survivor disappears exactly when `q|a`. Writing `a=qb`, and using `(q,N_x)=1`,

\[
(a,N_x)=1
\iff
(b,N_x)=1.
\tag{6}
\]

Conversely every `b` counted on the right of (5) produces an old survivor `qb` that is removed after adjoining `q`. No asymptotic argument is involved.

Equation (5) is the set-level one-prime Buchstab/Eratosthenes recursion. It also gives the exact cardinality relation

\[
\boxed{
|R_x^+(H)|
=
|R_x(H)|-|R_x(\lfloor H/q\rfloor)|.
}
\tag{7}
\]

Thus the most immediate cross-level transport of the primitive boundary is already the ordinary sieve update, not an additional geometric refinement law.

## 2. The entire prime-only window is a one-vertex deletion

If

\[
H<q^2,
\tag{8}
\]

then `R_x(\lfloor H/q\rfloor)={1}`. To see this, any integer `b>1` coprime to `N_x` has least prime factor strictly larger than `x`, hence at least `q`; but `b<H/q<q`. Therefore (5) reduces to

\[
\boxed{
R_x^+(H)=R_x(H)\setminus\{q\}
\qquad(H<q^2).
}
\tag{9}
\]

This applies throughout the nontrivial prime-only mesoscopic regime of PC-388. Fix `1<u<2` and put

\[
H_x=x^u.
\tag{10}
\]

For sufficiently large `x`, Bertrand's postulate gives `q<2x<H_x`, while `H_x<x^2\le q^2`. Hence `q` lies in the window and is the **only** primitive boundary vertex removed when passing from `N_x` to `qN_x`:

\[
\boxed{
R_x^+(x^u)=R_x(x^u)\setminus\{q\},
\qquad 1<u<2,
}
\tag{11}
\]

for all sufficiently large `x`.

At the first composite threshold the recursion changes exactly as the rough-number hierarchy predicts. At `H=q^2`, the deleted set is `\{q,q^2\}`; above it, the additional deleted points are `q` times old rough numbers. This is not a new cross-level arithmetic species: it is the same Buchstab hierarchy already present in the support description of PC-388.

## 3. Pairwise chord-kernel transport becomes a principal-minor update

The support recursion has a direct spectral consequence for the simplest line-forced boundary operator. Fix `alpha>0` and `tau>0`, and use the normalized regularized inverse-chord kernel from the PC-386/PC-388 mesh analysis,

\[
\kappa_N(d)
:=
N^{-2\alpha}
\left[
2\left(\cosh\frac{\tau}{N}-\cos\frac{2\pi d}{N}\right)
\right]^{-\alpha}.
\tag{12}
\]

For a boundary support `R`, let `K_N[R]` be the Hermitian pairwise kernel matrix

\[
(K_N[R])_{a,b}:=\kappa_N(a-b),
\qquad a,b\in R.
\tag{13}
\]

This statement concerns the pairwise kernel matrix itself. A degree-renormalized graph Laplacian has an additional diagonal response when a vertex is deleted and is not claimed to be a principal minor.

Set

\[
A_x:=K_{N_x}[R_x(H_x)],
\qquad
A_x^+:=K_{qN_x}[R_x^+(H_x)].
\tag{14}
\]

For `1<u<2`, let `C_x` be the principal submatrix of `A_x` obtained by deleting the coordinate `q`. By (11), `C_x` and `A_x^+` have exactly the same index set. Their only difference is the conductor used inside the chord kernel.

PC-388 gives uniformly for `|d|\le H=o(N)`

\[
\kappa_N(d)
=
(\tau^2+4\pi^2d^2)^{-\alpha}
\left(1+O_{\alpha,\tau}\!\left(\frac{1+d^2}{N^2}\right)\right).
\tag{15}
\]

Consequently, using the maximum row-sum bound for the operator norm,

\[
\|A_x^+-C_x\|_{\rm op}
\ll_{\alpha,\tau}
\frac{1}{N_x^2}
\sum_{0\le d\le H_x}
(1+d^2)(\tau^2+4\pi^2d^2)^{-\alpha}.
\tag{16}
\]

The sum on the right is

\[
O_{\alpha,\tau}(G_\alpha(H_x)),
\qquad
G_\alpha(H):=
\begin{cases}
H^{3-2\alpha},&0<\alpha<3/2,\\
\log(2+H),&\alpha=3/2,\\
1,&\alpha>3/2.
\end{cases}
\tag{17}
\]

Since `H_x=x^u` grows only polynomially while `N_x` grows exponentially in `x`,

\[
\boxed{
\|A_x^+-C_x\|_{\rm op}\longrightarrow0.
}
\tag{18}
\]

Thus the genuine prime-circle operator on the next primorial boundary is asymptotically the principal minor of the preceding operator obtained by deleting the single vertex `q`.

Equivalently, if `P_q` denotes the coordinate projection on `\ell^2(R_x(H_x))` that kills `e_q`, and `J_x` embeds the new boundary space by zero extension, then

\[
A_x-J_xA_x^+J_x^*
=
\bigl(A_x-P_qA_xP_q\bigr)+o_{\rm op}(1),
\tag{19}
\]

and

\[
\boxed{
\operatorname{rank}\bigl(A_x-P_qA_xP_q\bigr)\le2.
}
\tag{20}
\]

The rank bound is elementary because the range of `A_x-P_qA_xP_q` is contained in `\operatorname{span}\{e_q,A_xe_q\}`.

## 4. Spectral consequence: asymptotic Cauchy interlacing

Let the eigenvalues of the Hermitian `m_x\times m_x` matrix `A_x` be ordered increasingly,

\[
\lambda_1(A_x)\le\cdots\le\lambda_{m_x}(A_x),
\tag{21}
\]

and let those of the `(m_x-1)\times(m_x-1)` matrix `A_x^+` be

\[
\lambda_1(A_x^+)\le\cdots\le\lambda_{m_x-1}(A_x^+).
\tag{22}
\]

Cauchy's interlacing theorem applies exactly to the principal minor `C_x`:

\[
\lambda_j(A_x)
\le
\lambda_j(C_x)
\le
\lambda_{j+1}(A_x).
\tag{23}
\]

Weyl perturbation together with (18) then gives uniformly in `j`

\[
\boxed{
\lambda_j(A_x)-\varepsilon_x
\le
\lambda_j(A_x^+)
\le
\lambda_{j+1}(A_x)+\varepsilon_x,
\qquad
\varepsilon_x\to0.
}
\tag{24}
\]

So in the whole regime `1<u<2`, the canonical same-window spectral evolution from one primorial to the next is asymptotically constrained by the most elementary principal-minor interlacing mechanism. The only new row/column removed is the one indexed by the next prime already selected by the sieve support.

This does not make the deleted row numerically trivial: its entries encode the deterministic chord kernel evaluated at the gaps from `q` to the other retained rough/prime indices. The point is narrower. **The cross-level step itself contributes no independent distributed interaction law** beyond that support-selected vertex and the already-fixed pairwise kernel.

## 5. Prior-art and novelty audit

The arithmetic recursion (5) is a direct specialization of the classical Buchstab sieve identity to adjoining one new sieving prime. Halberstam--Richert, **Sieve Methods** (1974), and the rough-number references already anchored for PC-388 cover this sieve structure. The `H<q^2` collapse to a single deleted point is the same least-prime-factor threshold used in PC-388.

The spectral ingredient is also classical linear algebra: deletion of one coordinate produces a principal submatrix, whose Hermitian spectrum obeys Cauchy interlacing; an `o(1)` operator-norm perturbation changes each ordered eigenvalue by `o(1)` through the standard Weyl bound. The rank-two identity (20) is elementary.

PC-149 already shows that fixed words in full-period primitive compressed translations reduce by CRT to generalized-totient/Hardy--Littlewood tuple data. PC-389 is not a new arithmetic identity beyond that family. Its distinct line-specific role is to address the **mesoscopic successive-primorial boundary transport left open by PC-388**: before rough composites enter, that transport is exactly one sieve deletion, and the normalized pairwise chord-kernel operator follows it by asymptotic principal-minor compression.

No novel zeta or RH mechanism is claimed. The result is a classicalization/no-go boundary: simply comparing spectra of the same anchored boundary window across successive primorial shells does not by itself add a new geometric coupling.

## 6. Boundaries and falsification checks

The result has several deliberate boundaries.

First, (5) is exact for the same anchored exponent window, but the one-vertex simplification (9) requires `H<q^2`. Once rough composites enter, the deleted set is the larger recursively defined set `qR_x(H/q)`.

Second, the spectral statement concerns pairwise Hermitian kernel matrices `K_N[R]`. A graph Laplacian, Schur complement, nonlinear functional, or operator whose coefficients depend on the shell in some additional way can respond differently to vertex deletion.

Third, the `o(1)` comparison uses a polynomial boundary window and the locally Euclideanized normalized chord kernel. It does not classify windows occupying a macroscopic fraction of the polygon or operators whose range/depth grows fast enough to defeat that local approximation.

Fourth, principal-minor interlacing does not imply that the deleted row contains no useful arithmetic. It only shows that the natural successive-level transport has no extra distributed degree of freedom beyond a support-selected one-vertex update in this regime.

The exact support claim can be falsified at finite level by choosing any primorial `N_x`, adjoining `q`, and checking that the old survivors lost below `H` are precisely `q` times the old survivors below `H/q`. The operator claim can be audited numerically by forming the two normalized chord-kernel matrices, deleting the `q` row/column from the old one, and measuring the operator-norm difference; on polynomial windows it must tend to zero at the rate implied by (16)--(17).

## Consequence for the research line

PC-388 showed that the primorial boundary support itself is the classical rough-number wheel and explicitly left cross-level transport as a possible escape. PC-389 closes the most canonical version of that escape in the prime-only mesoscopic zone: keeping the same anchored window while adjoining the next primorial factor is a one-point Buchstab deletion, and the normalized pairwise chord-kernel spectrum changes asymptotically by principal-minor interlacing.

A viable cross-level continuation must therefore use more than same-window inclusion/compression of a fixed pairwise kernel. It must introduce a source-forced correspondence that is not equivalent to Buchstab deletion plus local Euclidean chord evaluation—for example a genuinely nonlocal fiber map, growing-depth history, nonlinear cross-level invariant, or another coupling whose residue survives after the rough-number support and the one-vertex update are factored out.