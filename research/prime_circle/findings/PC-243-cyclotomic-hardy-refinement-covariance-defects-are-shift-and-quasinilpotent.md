# PC-243 — cyclotomic Hardy refinement covariance defects are shift and quasinilpotent

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the most direct shell-dependent one-sided repair left open by PC-242: combine the positive Hardy scaling Hamiltonian with the exact cyclotomic-weighted refinement from PC-209 and ask whether the resulting covariance defects carry a new Prime-Circle spectral invariant. They do not. The number-operator defect is, after one scalar normalization, the universal pure shift of countably infinite multiplicity; the logarithmic-Hamiltonian remainder is compact Hilbert--Schmidt, quasinilpotent, and has spectrum `{0}` with trivial regularized determinant. Its apparent Schatten threshold at `Re(s)=1/2` is the universal `1/k` singular-value tail of finite-width refinement blocks, not an RH critical-line mechanism.

The result is deliberately narrow. It classifies these **canonical single-shell covariance defects**. It does not classify the full pair consisting of the Hamiltonian and all cyclotomic-weighted refinements jointly, nor relational products/commutators between distinct conductors, localized tube geometry, nonlinear/off-circle harmonic interactions, simultaneous-growth limits, or global uniformization/accessory data.

## 1. Question and intrinsic weighted Hardy refinement

Work on the positive Hardy sector

\[
\mathcal H_+=zH^2(S^1),
\qquad
e_k(z)=z^k,\quad k\ge1.
\tag{1}
\]

Let

\[
Ne_k=k e_k,
\qquad
H=\log N,
\qquad
He_k=(\log k)e_k.
\tag{2}
\]

PC-242 shows that the bare refinement isometry `C_n e_k=e_{nk}` satisfies

\[
HC_n-C_nH=(\log n)C_n
\tag{3}
\]

and that this is exactly the Bost--Connes scaling Hamiltonian. PC-209 leaves open a natural shell-dependent repair: retain the exact primitive-shell polynomial before diagonalization. Write

\[
\Phi_n(z)=\sum_{j=0}^{d_n}a_{n,j}z^j,
\qquad
d_n=\varphi(n)<n,
\tag{4}
\]

and define

\[
h_n:=\sum_{j=0}^{d_n}|a_{n,j}|^2,
\qquad
\kappa_n:=\sum_{j=1}^{d_n}j^2|a_{n,j}|^2.
\tag{5}
\]

The normalized cyclotomic-weighted cover is

\[
V_n:=h_n^{-1/2}M_{\Phi_n}C_n,
\tag{6}
\]

so

\[
V_ne_k
=h_n^{-1/2}\sum_{j=0}^{d_n}a_{n,j}e_{nk+j}.
\tag{7}
\]

Because `d_n<n`, the output blocks `[nk,nk+d_n]` for distinct `k` are disjoint. PC-209 therefore gives `V_n^*V_n=I`. The present question is whether inserting the shell multiplier into the exact number/scaling covariance creates a genuinely new operator carrier that survives the matched controls demanded by the Prime-Circle mandate.

## 2. The number-covariance defect is again a universal pure shift

On the finite Fourier core define

\[
D_n:=NV_n-nV_nN.
\tag{8}
\]

Using (7),

\[
\boxed{
D_n
=h_n^{-1/2}M_{z\Phi_n'}C_n,
}
\tag{9}
\]

and

\[
D_ne_k
=h_n^{-1/2}
\sum_{j=1}^{d_n}j a_{n,j}e_{nk+j}.
\tag{10}
\]

The same block separation that made `V_n` an isometry now gives

\[
\boxed{
D_n^*D_n=\frac{\kappa_n}{h_n}I.
}
\tag{11}
\]

Thus

\[
S_n:=\sqrt{\frac{h_n}{\kappa_n}}D_n
\tag{12}
\]

is an isometry. It is pure: every application strictly raises the Fourier index, so the decreasing range intersection is zero. Its range has infinite codimension because every length-`n` output block contains at most one range vector. Hence its wandering multiplicity is countably infinite, and Wold--von Neumann gives

\[
\boxed{
S_n\simeq S^{(\aleph_0)},
\qquad
D_n\simeq
\sqrt{\frac{\kappa_n}{h_n}}\,S^{(\aleph_0)}.
}
\tag{13}
\]

The complete abstract unitary class of this first covariance defect therefore retains only the coefficient-moment ratio `kappa_n/h_n`. Increasing from the shell-weighted cover itself in PC-209 to its canonical number commutator does not create a new spectral species.

There is also an exact doubled-conductor control. For odd `n>1`, the classical identity

\[
\Phi_{2n}(z)=\Phi_n(-z)
\tag{14}
\]

implies `h_{2n}=h_n` and `kappa_{2n}=kappa_n`. If `R e_m=(-1)^m e_m` is the parity unitary and `C_2e_k=e_{2k}`, then

\[
\boxed{D_{2n}=R D_n C_2.}
\tag{15}
\]

Both sides of (13) therefore have the same scalar and the same pure-shift multiplicity for `n` and `2n`. In particular a prime `p` and the composite `2p` are unitarily indistinguishable by the full number-covariance defect, not merely by a chosen trace or moment.

## 3. The logarithmic covariance remainder has exact singular data

The more relevant test uses the additive scaling Hamiltonian from PC-242. Remove the bare Bost--Connes shift and define

\[
K_n:=HV_n-V_nH-(\log n)V_n.
\tag{16}
\]

Equation (7) gives the exact basis action

\[
\boxed{
K_ne_k
=h_n^{-1/2}
\sum_{j=1}^{d_n}
a_{n,j}
\log\!\left(1+\frac{j}{nk}\right)
e_{nk+j}.
}
\tag{17}
\]

Again the columns occupy pairwise disjoint blocks. Therefore `K_n^*K_n` is diagonal:

\[
\boxed{
K_n^*K_ne_k=q_{n,k}e_k,
}
\tag{18}
\]

where

\[
\boxed{
q_{n,k}
=\frac1{h_n}
\sum_{j=1}^{d_n}|a_{n,j}|^2
\log^2\!\left(1+\frac{j}{nk}\right).
}
\tag{19}
\]

Consequently the singular values are exactly `sqrt(q_{n,k})`, up to decreasing rearrangement. Since the sum over `j` is finite,

\[
q_{n,k}
=
\frac{\kappa_n}{h_n n^2}\frac1{k^2}
+O(k^{-3}),
\tag{20}
\]

and hence

\[
\boxed{
s_k(K_n)\sim
\frac1n\sqrt{\frac{\kappa_n}{h_n}}\,\frac1k.
}
\tag{21}
\]

Thus `K_n` is compact and

\[
\boxed{
K_n\in\mathcal S_r
\quad\Longleftrightarrow\quad r>1.
}
\tag{22}
\]

In particular it is Hilbert--Schmidt but not trace class, while `K_n^*K_n` is trace class. One can manufacture the Dirichlet-type quantity

\[
\operatorname{Tr}\big((K_n^*K_n)^s\big)
=\sum_{k\ge1}q_{n,k}^s,
\tag{23}
\]

whose elementary convergence boundary is `Re(s)>1/2`. Equation (20) shows exactly why this is **not** evidence for the Riemann critical line: the boundary is forced by the universal `k^{-2}` tail of any finite-width weighted refinement block. No zeta zero, functional equation, gamma factor, or prime-specific cancellation has entered.

## 4. The logarithmic remainder is quasinilpotent

The spectrum collapses more strongly than the singular values suggest. Since `log(1+x)<=x` for `x>=0`, (19) yields

\[
q_{n,k}
\le
\frac{\kappa_n}{h_n n^2}\frac1{k^2}.
\tag{24}
\]

Set

\[
C_n^{\mathrm{def}}:=\frac1n\sqrt{\frac{\kappa_n}{h_n}}.
\tag{25}
\]

For the tail subspace

\[
\mathcal H_{\ge M}:=\overline{\operatorname{span}}\{e_k:k\ge M\},
\]

orthogonality of the columns and (24) give

\[
\left\|K_n\big|_{\mathcal H_{\ge M}}\right\|
\le \frac{C_n^{\mathrm{def}}}{M}.
\tag{26}
\]

Every nonzero term in (17) also raises degree from `k` to at least `nk+1`, so

\[
K_n\mathcal H_{\ge M}
\subseteq
\mathcal H_{\ge nM+1}
\subseteq
\mathcal H_{\ge nM}.
\tag{27}
\]

Iterating (26)--(27) from `M=1` gives

\[
\boxed{
\|K_n^m\|
\le
(C_n^{\mathrm{def}})^m
n^{-m(m-1)/2}.
}
\tag{28}
\]

Therefore

\[
\boxed{
r(K_n)=0.}
\tag{29}
\]

Since `K_n` is compact,

\[
\boxed{\operatorname{Spec}(K_n)=\{0\}.}
\tag{30}
\]

The most direct spectral-determinant wrapper is correspondingly empty. Because `K_n` is Hilbert--Schmidt, its Carleman--Fredholm determinant `det_2(I-zK_n)` is defined. All eigenvalues of the compact operator are zero, hence

\[
\boxed{\det_2(I-zK_n)=1\qquad(z\in\mathbb C).}
\tag{31}
\]

Equivalently, `K_n^m` is trace class for every `m>=2`, strictly raises Fourier degree, and therefore has zero trace. The logarithmic shell correction can have nontrivial singular values and nonnormal geometry while carrying **no nonzero eigenvalue at all**.

## 5. Doubled-conductor and nonarithmetic controls

For odd `n>1`, the same parity identity (14) gives an exact relation for the logarithmic remainder:

\[
\boxed{K_{2n}=R K_n C_2.}
\tag{32}
\]

Consequently

\[
\boxed{q_{2n,k}=q_{n,2k}.}
\tag{33}
\]

Unlike the number defect, this does not make `K_n` and `K_{2n}` unitarily equivalent: it says that the composite `2n` singular data are literally the even-index subsequence of the `n` data, up to a unitary output parity. For a prime `p`, the `2p` control therefore produces no independent logarithmic-covariance sequence; it is a deterministic subsampling of the prime-level one.

More decisively, none of the structural conclusions above requires cyclotomy. Let

\[
P(z)=\sum_{j=0}^{d}b_jz^j,
\qquad
1\le d<n,
\tag{34}
\]

be any nonconstant polynomial, put `h(P)=sum_j |b_j|^2`, and replace `Phi_n` in (6) by `P`. The same disjoint-block derivation gives:

- the normalized weighted cover is an isometry;
- its number-covariance defect is a scalar multiple of a pure shift of countably infinite multiplicity;
- its logarithmic remainder has exact diagonal `K^*K`, singular values asymptotic to `const/k`, the Schatten threshold `r>1`, spectral radius zero, spectrum `{0}`, and `det_2(I-zK)=1`.

Thus the shift collapse, compactness, quasinilpotence, and the apparent half-plane boundary in (23) are consequences of `deg P<n` and one-sided block separation. Cyclotomic coefficients change finite singular data and scalar moments, but they do not create the operator-theoretic phenomenon itself. This matched arbitrary-polynomial control is stronger than a prime-versus-composite comparison.

## 6. Prior-art and novelty audit

The operator ingredients are classical. PC-209 already audits weighted composition operators on Hardy space and the Wold--von Neumann classification, and proves the pure-shift collapse for the exact cyclotomic-weighted cover `M_{Phi_n}C_n`. PC-242 identifies the one-sided logarithmic number Hamiltonian and its bare power-refinement covariance exactly with the canonical Bost--Connes representation. The cyclotomic identity (14) is standard.

A targeted literature check against weighted-composition operators, composition/differentiation operators on Hardy spaces, compact/Schatten questions, and the Bost--Connes scaling representation found a mature classical operator-theory neighborhood but no evidence that the present project-specific covariance remainder supplies an independent zeta-zero mechanism. The negative conclusion does not depend on that absence: equations (11), (28), and (30)--(33) are exact and the arbitrary-polynomial control (34) reproduces the decisive features without arithmetic input.

No novelty is claimed for weighted composition operators, Wold decomposition, Hardy number operators, compact/quasinilpotent weighted shifts, regularized determinants, or the cyclotomic parity identity. The durable Prime-Circle contribution is the **boundary statement** that the most direct shell-weighted covariance repair of PC-242 still fails: at first order the shell correction is only a universal pure shift up to one coefficient moment, while at logarithmic scale its natural remainder has trivial spectrum and a nonarithmetic Schatten tail.

## 7. Boundary of the obstruction and research consequence

This is not a no-go for the complete family `({V_n},H)` with every conductor retained jointly. The individual `K_n` still remembers coefficient magnitudes in its finite singular sequence and coefficient signs/phases in the directions of its output blocks; those data are not classified away by (30). Likewise, products or commutators involving **distinct** `V_m` and `V_n` can compare incompatible cyclotomic block directions and are outside the theorem. The result also does not touch the accepted localized preimage-tube clue, genuinely nonlinear/off-circle harmonic interactions, simultaneous conductor-depth growth, or global uniformization/accessory parameters.

What it does close is the canonical chain

\[
\boxed{
\Phi_n\text{-weighted Hardy refinement}
\longrightarrow
\text{single-shell covariance defect against }N\text{ or }\log N
\longrightarrow
\text{new spectral/RH carrier}.
}
\tag{35}
\]

A surviving one-sided Prime-Circle mechanism must therefore use **relational information before single-shell spectral compression**: cross-conductor products/commutators, source-forced scale-dependent mode coupling, a genuinely localized geometric event, nonlinear harmonic interaction, or another construction whose decisive invariant fails the arbitrary-polynomial and `n<->2n` controls above.

## Falsification checks

The exact negative can be audited without numerical inference. A counterexample must break at least one of the following direct tests: verify (9)--(11) from the monomial basis and `deg Phi_n<n`; verify purity and infinite wandering multiplicity in (13); verify the exact diagonal formula (18)--(19); check the tail expansion (20); derive the tail-norm iteration (26)--(28); verify the odd-conductor relations (15) and (32); and repeat the derivation with an arbitrary noncyclotomic polynomial of degree `<n`. Failure of any asserted identity changes the conclusion; otherwise the single-shell covariance-defect branch is decisively closed.