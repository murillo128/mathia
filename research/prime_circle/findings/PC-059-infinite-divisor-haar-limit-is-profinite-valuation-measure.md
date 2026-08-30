# PC-059 — infinite divisor-Haar limit is the profinite valuation measure

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-REDIRECTION` + `NEGATIVE` for interpreting the infinite-volume completion of the fixed divisor-Haar basis from PC-058 as a new pure-point or Hilbert–Pólya spectrum. The finite divisor-box eigenvectors have an exact projective-limit spectral measure: seen from the birth vacuum `n=1`, their weights are precisely the truncated `p`-adic valuation probabilities of a uniform residue. Passing to all prime powers gives the product valuation law obtained by pushing normalized Haar measure on the profinite integers `hat Z = prod_p Z_p` through the valuation map. This limiting joint measure is nonatomic, and the factorwise pure eigenvectors leave the ordinary arithmetic incomplete-tensor sector at the classical Mertens/Euler `s=1` rate.

This is a genuine infinite-volume change relative to PC-058: finite pure-point diagonalizations converge to a continuous product spectral representation. What is negative is the RH interpretation. The measure and the sector change are classical profinite/infinite-tensor phenomena and introduce neither a free complex spectral parameter nor a functional-equation symmetry or critical-line selector.

## 1. The local divisor-Haar vacuum weights are exactly geometric valuation probabilities

PC-058 diagonalizes, on the prime-power divisor box

\[
\mathcal D(p^A)=\{1,p,\ldots,p^A\},
\]

the normalized birth matrices

\[
S_f=D_p^{-1/2}M_pK_fM_p^{\mathsf T}D_p^{-1/2},
\qquad
D_p=\operatorname{diag}(\varphi(p^a))_{a=0}^A,
\]

in one basis independent of the scalar kernel `f`. Its generalized vectors before shell normalization are

\[
v_{p,*}=(1,\ldots,1)^{\mathsf T}
\]

and, for `0<=j<A`,

\[
(v_{p,j})_a=
\begin{cases}
1-p,&0\le a\le j,\\
1,&a=j+1,\\
0,&a>j+1.
\end{cases}
\]

with exact `D_p` norms

\[
v_{p,*}^{\mathsf T}D_pv_{p,*}=p^A,
\qquad
v_{p,j}^{\mathsf T}D_pv_{p,j}=(p-1)p^{j+1}.
\]

Choose phases and normalize the ordinary eigenvectors by

\[
u_{p,*}=\frac{D_p^{1/2}v_{p,*}}{p^{A/2}},
\qquad
u_{p,j}=-\frac{D_p^{1/2}v_{p,j}}
{\sqrt{(p-1)p^{j+1}}}.
\]

Let `e_0` denote the coordinate of the shell `1`. Since `D_p(0,0)=phi(1)=1`, direct inspection of the first coordinate gives

\[
\boxed{
|\langle e_0,u_{p,*}\rangle|^2=p^{-A},
}
\]

and

\[
\boxed{
|\langle e_0,u_{p,j}\rangle|^2
=\frac{p-1}{p^{j+1}}
=\left(1-\frac1p\right)p^{-j},
\qquad 0\le j<A.
}
\]

The weights sum to one:

\[
p^{-A}+\sum_{j=0}^{A-1}\frac{p-1}{p^{j+1}}=1.
\]

These are not merely reminiscent of `p`-adic probabilities. If `X` is uniform in `Z/p^A Z`, define the truncated valuation label

\[
J_{p,A}(X)=
\begin{cases}
j,&v_p(X)=j<A,\\
*,&X\equiv0\pmod{p^A}.
\end{cases}
\]

Then exactly

\[
\boxed{
\Pr(J_{p,A}=j)=\frac{p-1}{p^{j+1}},
\qquad
\Pr(J_{p,A}=*)=p^{-A}.
}
\]

Therefore the local spectral measure of the arithmetic vacuum in the PC-058 eigenbasis is exactly the valuation distribution of a uniform residue modulo `p^A`.

## 2. On every divisor box the full joint spectral measure is uniform-residue valuation data

Let

\[
N=\prod_{p\mid N}p^{A_p}.
\]

PC-058 shows that the common eigenbasis on `D(N)` is the tensor product of the local divisor-Haar bases. The shell `1` is likewise the tensor vacuum

\[
e_1=\bigotimes_{p\mid N}e_{p,0}.
\]

Hence the squared overlap with a joint eigenlabel `alpha=(alpha_p)` factorizes:

\[
\boxed{
|\langle e_1,u_{\boldsymbol\alpha}\rangle|^2
=\prod_{p\mid N}w_{p,A_p}(\alpha_p),
}
\]

where

\[
w_{p,A}(j)=\frac{p-1}{p^{j+1}},
\qquad
w_{p,A}(*)=p^{-A}.
\]

By the Chinese remainder theorem, a uniform residue `X mod N` has independent components modulo each `p^{A_p}`. Consequently

\[
\boxed{
\text{PC-058 joint vacuum spectral measure on }\mathcal D(N)
=
\text{law of }(J_{p,A_p}(X))_{p\mid N}
\text{ for }X\text{ uniform mod }N.
}
\]

This is an exact finite statement, not an asymptotic model. For example, when `N=12=2^2*3`, the six joint weights are exactly the six CRT frequencies of the pair consisting of the truncated `2`- and `3`-adic valuations of a uniform residue modulo `12`.

## 3. The projective limit is the valuation pushforward of Haar measure on `hat Z`

The finite measures are projectively consistent. Increasing `A` by one splits the old terminal state by

\[
p^{-A}
=
\frac{p-1}{p^{A+1}}+p^{-(A+1)},
\]

which is exactly the split

\[
v_p(X)\ge A
\quad\rightsquigarrow\quad
v_p(X)=A
\text{ or }
v_p(X)\ge A+1.
\]

Adding a new prime simply tensors with a probability distribution of total mass one. Thus the finite joint measures have the canonical product limit

\[
\boxed{
\mu=\bigotimes_p\mu_p
\quad\text{on}\quad
\Omega=\prod_p\mathbb N_0,
}
\]

with

\[
\boxed{
\mu_p(j)=\left(1-\frac1p\right)p^{-j}.
}
\]

Now use the classical factorization of the profinite integers

\[
\widehat{\mathbb Z}\cong\prod_p\mathbb Z_p
\]

with normalized additive Haar probability. Since

\[
m_p(p^j\mathbb Z_p)=p^{-j},
\]

we have

\[
m_p\{x:v_p(x)=j\}
=p^{-j}-p^{-(j+1)}
=\mu_p(j).
\]

The exceptional point `x_p=0`, where the valuation is infinite, has Haar measure zero. Therefore

\[
\boxed{
\mu
=(v_p)_*\,m_{\widehat{\mathbb Z}},
}
\]

where the right-hand side means the pushforward of Haar measure by the coordinatewise valuation map, modulo the null set of infinite local valuations.

So the infinite completion selected by the finite prime-circle divisor-Haar weights is not an unexplained new probability space. It is the **valuation quotient of profinite Haar measure**.

## 4. Finite pure-point spectra become a nonatomic joint representation

Although every finite divisor box has a finite orthogonal eigenbasis, the limiting measure has no atoms. For any point `omega=(j_p)_p in Omega`,

\[
\mu(\{\omega\})
=\prod_p\left(1-\frac1p\right)p^{-j_p}
\le
\prod_p\left(1-\frac1p\right)
=0.
\]

The last product vanishes already by the classical divergence of `sum_p 1/p`; Mertens' prime-product theorem gives the sharper finite-stage rate

\[
\boxed{
\prod_{p\le P}\left(1-\frac1p\right)
\sim\frac{e^{-\gamma}}{\log P}.
}
\]

In particular, valuation vectors with finite prime support—the vectors corresponding to ordinary positive integers—form a countable `mu`-null set. More strongly, the independent events `J_p>0` have probabilities `1/p`, so the second Borel-Cantelli lemma gives

\[
\boxed{
J_p>0\text{ for infinitely many primes }p
\quad\text{for }\mu\text{-almost every label}.}
\]

Typical joint spectral labels are therefore supernatural/profinite divisibility patterns, not ordinary integer shell labels.

There is a canonical Hilbert-space way to state the same result. For fixed `p`, the vectors `u_{p,j}` with finite `j` are independent of the cutoff once `A>j`, and as `A->infinity` they form a complete orthonormal basis of the local exponent space: the remaining normalized `*` vector has unit norm but escapes weakly to infinity. After choosing the phases above, the local spectral transform can therefore be normalized so that

\[
e_{p,0}\longmapsto1
\quad\text{in}\quad
L^2(\mathbb N_0,\mu_p).
\]

The compatible infinite tensor product therefore gives the joint spectral representation

\[
\boxed{
\ell^2(\mathbb N)
\simeq
L^2(\Omega,\mu),
}
\]

where `ell^2(N)` is understood in the prime-exponent tensor coordinates underlying the normalized birth space, and the shell `1` maps to the constant function `1`. The finite diagonal matrices become cylinder multiplication operators. The global joint spectral representation is thus continuous/nonatomic even though each finite truncation is pure point.

This does **not** imply that every individual infinite operator has purely continuous spectrum: a multiplication function can be constant on a positive-measure set. The exact conclusion concerns the joint divisor-Haar spectral measure and the disappearance of an atomic eigenbasis indexed by ordinary arithmetic shells.

## 5. The naive factorwise eigenvector synthesis leaves the arithmetic tensor sector

The same obstruction is visible directly in von Neumann's incomplete infinite tensor product. Consider the locally most vacuum-aligned eigenvector `u_{p,0}`. Its overlap with the local arithmetic vacuum is

\[
|\langle e_{p,0},u_{p,0}\rangle|
=\sqrt{1-\frac1p}.
\]

For the primorial box `P#=prod_{p<=P}p`, the all-`j=0` eigenvector therefore has vacuum overlap

\[
\boxed{
|\langle e_1,u_{0,P}\rangle|^2
=\prod_{p\le P}\left(1-\frac1p\right)
=\frac{\varphi(P\#)}{P\#}.
}
\]

This tends to zero. Equivalently,

\[
\sum_p\left(1-\sqrt{1-\frac1p}\right)=\infty.
\]

By the classical equivalence criterion for incomplete infinite tensor products, the reference sequence `(u_{p,0})_p` is not strongly equivalent to `(e_{p,0})_p`. Hence the formal product of local pure eigenvectors does not define a vector in the original arithmetic incomplete-tensor sector. Any other fixed pure joint label has no better overlap, because `j=0` maximizes every local vacuum weight.

This is precisely compatible with the nonatomic measure above: the correct global diagonalization is a direct/product spectral representation, not a countable tensor product of normalizable point eigenvectors inside the original sector.

## 6. Why this is not a critical-line mechanism

The infinite limit does something real: it converts the finite divisor-Haar basis into a classical continuous product spectrum. But the only global decay used to destroy atoms and the pure product eigenvectors is

\[
\prod_p(1-p^{-1})=0,
\]

or quantitatively Mertens' theorem at the ordinary Euler-product boundary `s=1`. No location of nontrivial zeta zeros enters.

Likewise the local probabilities are fixed algebraically by

\[
\mu_p(j)=(1-p^{-1})p^{-j}.
\]

They provide no free complex parameter, no gamma factor, no intrinsic `s <-> 1-s` involution and no distinguished `Re(s)=1/2`. A Mellin transform, adelic Fourier transform, or weighted product can certainly be imposed afterward and can then generate classical Euler products. But that would be additional analytic structure, exactly as in the prior-art boundaries already exposed by PC-010, PC-054 and PC-055.

The route

\[
\boxed{
\text{finite divisor-Haar eigenbasis}
\to
\text{take all prime/refinement levels}
\to
\text{new discrete zeta-zero spectrum}
}
\]

therefore fails. The canonical infinite completion is instead

\[
\boxed{
\text{finite divisor-Haar weights}
\to
\text{profinite valuation product measure}
\to
\text{nonatomic multiplication representation}.}
\]

There is one useful surviving boundary: `hat Z` is the finite-adic side of the standard adelic picture. To turn that observation into a functional-equation mechanism one would still have to derive, from prime-circle geometry itself, an archimedean component and a self-dual Fourier/Mellin structure rather than append Tate-style adelic machinery by hand. Nothing in the present theorem supplies that missing step.

## 7. Prior-art and novelty audit

Every ambient ingredient is classical.

- The compact group `hat Z` is the inverse limit of the finite residue rings and decomposes as `prod_p Z_p`; normalized Haar probability is the projective limit of uniform residue measures. The displayed geometric valuation law is the immediate consequence `m_p(p^j Z_p)=p^{-j}`.
- Independent prime-local divisibility variables and their geometric prime-power refinements are standard probabilistic-number-theory/Kubilius territory.
- The vanishing product `prod_p(1-1/p)` and its `e^{-gamma}/log P` asymptotic are the classical Euler/Mertens prime-product facts.
- The distinction between complete and incomplete infinite tensor products and the equivalence classes of reference product vectors is classical von Neumann theory. A convenient literature anchor is Huzihiro Araki and Yoshiomi Nakagami, **A Remark on an Infinite Tensor Product of von Neumann Algebras**, *Publ. RIMS* 8 (1972), 363–374, DOI `10.2977/PRIMS/1195193114`.
- PC-010 already places the abstract all-level cyclotomic refinement tower in the Bost-Connes/profinite cyclotomic setting, so landing on a profinite arithmetic probability space is a prior-art redirection, not evidence of a new zeta dynamics.

No historical novelty is claimed for profinite Haar measure, valuation probabilities, Mertens' product, Borel-Cantelli, or infinite tensor products. The durable prime-circle contribution is the exact project-specific identification:

\[
\boxed{
\text{the vacuum weights of the PC-058 divisor-Haar eigenbasis are exactly the finite residue valuation laws, and their canonical all-level limit is the nonatomic profinite valuation measure.}
}
\]

That closes a specific infinite-completion ambiguity left by PC-058 while exposing a precise finite-adic boundary for any future attempt to derive a functional equation intrinsically.

## 8. Boundaries and exact falsification tests

The result does **not** rule out:

- an infinite operator whose multiplication symbol on `(Omega,mu)` has a separately derived nontrivial spectrum;
- a different intrinsic two-dimensional kernel that does not lie in the PC-058 fixed divisor-Haar algebra;
- nonlinear coupling before passage to the divisor-Haar representation;
- an intrinsically derived archimedean/finite-adic pairing with a genuine self-duality;
- or the global primitive-root uniformization/accessory branch of PC-017.

It does rule out reading the mere all-level completion of the PC-058 finite eigenvectors as a new countable Hilbert–Pólya eigenbasis.

The claim has finite and projective checks:

1. compute the first coordinate and `D_p` norm of every PC-058 local eigenvector and recover the two boxed weights;
2. count exact `p`-adic valuations of residues modulo `p^A` and compare them with those weights;
3. tensor over prime powers and use CRT to recover the complete vacuum spectral measure on `D(N)`;
4. increase `A` and verify the exact terminal-state splitting `p^{-A}=(p-1)p^{-(A+1)}+p^{-(A+1)}`;
5. identify the inverse-limit cylinder probabilities with Haar measure on `prod_p Z_p`;
6. use `sum_p 1/p=infinity` to prove that every singleton has zero mass and that the pure product eigenvectors are outside the arithmetic reference sector;
7. verify that no step invokes analytic continuation, a nontrivial zeta zero, or a critical-line symmetry.

Failure of the local overlap formula, the CRT product law, or the projective consistency would invalidate the identification. A future RH-positive continuation must add a geometrically forced operator on this profinite valuation representation (or leave it), not simply relabel the existing continuous product measure as a zeta spectrum.
