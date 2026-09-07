# PC-212 — common-refinement primitive-mask Gram is profinite and coprime-flat

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the canonical different-covering-degree escape left open by PC-211: lift direct primitive weighted covers to a common refinement before comparing them, retain all cyclotomic coefficient-mask data, and ask whether the resulting cross-level Hilbert/operator geometry creates a genuinely mixed prime carrier.

The canonical common-refinement lift does preserve more than the single same-level scalar of PC-211, but its structure is rigid. It is exactly the ordinary cylinder-function embedding into `L^2(hat Z)`. Every pairwise cross-transfer is central and is given by a finite cyclotomic root-of-unity Gram kernel. After removing the common Haar mode, the connected Gram coupling vanishes identically for coprime conductors. More sharply, the coefficient field attached to `Phi_n` has **zero Fourier component in the exact-order `n` sector**: all of its transverse Fourier mass lies on proper-divisor conductors. At prime levels every channel is literally the same Haar vector, and the entire prime-power sector orthogonalizes into independent prime-local Haar/valuation chains.

Thus the most direct way to retain different covering degrees by pushing their scalar cyclotomic masks to a common refinement does not produce a new mixed-prime operator sector. Any surviving cross-level mechanism must retain incidence/tensor data beyond this coefficient-mask Hilbert geometry, use a genuinely nonlinear operation, or exploit mixed-composite channels before they are reduced to pairwise Gram data.

## 1. Canonical common-refinement lift

Retain the notation of PC-209--PC-211:

\[
W_n=M_{\Phi_n}C_n,
\qquad
V_n=h_n^{-1/2}W_n,
\qquad
h_n=\|\Phi_n\|_{H^2}^2,
\]

and

\[
H_k=k^{-1/2}M_{S_k}C_k,
\qquad
S_k(z)=1+z+\cdots+z^{k-1}.
\]

For `n|N`, put `k=N/n` and define the normalized direct-primitive channel lifted to covering degree `N` by

\[
\boxed{
E_{n\to N}:=V_nH_k.
}
\tag{1}
\]

Because `C_nM_f=M_{f(z^n)}C_n`,

\[
E_{n\to N}
=
\frac{1}{\sqrt{h_nk}}
M_{\Phi_n(z)S_k(z^n)}C_N.
\tag{2}
\]

Write

\[
\Phi_n(z)=\sum_{r=0}^{n-1}a_n(r)z^r,
\tag{3}
\]

zero-padding the coefficient vector to length `n`. Then the length-`N` mask in (2) is simply

\[
\boxed{
\frac{1}{\sqrt{k h_n}}
\bigl(a_n(0),\ldots,a_n(n-1),
      a_n(0),\ldots,a_n(n-1),\ldots\bigr),
}
\tag{4}
\]

with exactly `k` repeated blocks. Since its squared norm is one, every `E_{n->N}` is an isometry.

The repetition map

\[
J_{n,N}:\mathbb C^n\to\mathbb C^N,
\qquad
(J_{n,N}x)_{qn+r}=\frac{x_r}{\sqrt{N/n}},
\tag{5}
\]

is itself an isometry and satisfies

\[
J_{N,M}J_{n,N}=J_{n,M}
\qquad(n|N|M).
\tag{6}
\]

Therefore the comparison of direct primitive masks across different covering degrees is not an arbitrary identification: the Haar refinement forced by PC-210 gives a coherent Hilbert direct system.

As the simplest nested consequence, PC-211's same-level scalar immediately propagates through every further refinement:

\[
\boxed{
V_n^*H_N
=c_nH_{N/n},
\qquad
c_n:=\frac{\Phi_n(1)}{\sqrt{nh_n}},
\qquad n|N.
}
\tag{7}
\]

So the direct primitive channel at level `n`, analyzed against the full Haar path at any finer multiple `N`, sees exactly the same normalized anchored scalar `c_n`; refinement depth adds only the universal remaining Haar isometry.

## 2. The direct limit is `L^2(hat Z)` and the primitive masks are cylinder functions

The isometries (5) are the usual pullbacks along the quotient maps

\[
\mathbb Z/N\mathbb Z\to\mathbb Z/n\mathbb Z.
\]

Their Hilbert direct limit is the space of locally constant functions in

\[
L^2(\widehat{\mathbb Z},m_{\mathrm H}),
\]

completed for normalized Haar probability `m_H`. Under the standard identification, the normalized cyclotomic coefficient mask becomes the cylinder function

\[
\boxed{
g_n(x)
=\sqrt{\frac{n}{h_n}}\,
a_n(x\bmod n),
\qquad x\in\widehat{\mathbb Z}.
}
\tag{8}
\]

Indeed,

\[
\|g_n\|_2^2
=\frac1n\frac{n}{h_n}
\sum_{r=0}^{n-1}a_n(r)^2
=1.
\tag{9}
\]

Thus the canonical infinite-depth state obtained by retaining all direct primitive coefficient masks under universal Haar refinement is not a new noncommutative fiber. It is an explicit family of ordinary periodic/cylinder functions on the profinite integers.

The Haar refinement channel itself is the constant unit vector

\[
\mathbf 1(x)=1.
\tag{10}
\]

Its overlap with `g_n` is

\[
\boxed{
\langle g_n,\mathbf 1\rangle
=\frac{\Phi_n(1)}{\sqrt{nh_n}}
=c_n,
}
\tag{11}
\]

so PC-211 is exactly the constant Fourier mode of this larger profinite realization.

## 3. Every common-refinement cross-transfer is a central cyclotomic Gram scalar

Let `m,n|N`. Both `E_{m->N}` and `E_{n->N}` are normalized masks in the same `N`-cover Cuntz block. The one-block cross-Gram lemma of PC-211 therefore gives

\[
\boxed{
E_{m\to N}^*E_{n\to N}
=\gamma_{m,n}I,
\qquad
\gamma_{m,n}=\langle g_m,g_n\rangle_{L^2(\widehat{\mathbb Z})}.
}
\tag{12}
\]

In particular, `gamma_{m,n}` is independent of which common multiple `N` is used. Refining farther cannot create a new principal-angle spectrum or operator-valued transfer: every pair remains isoclinic and all nontrivial data sit in one scalar positive-definite Gram kernel on conductor labels.

That kernel has an exact finite formula. Put

\[
d=(m,n)
\]

and define the coefficient sums in residue classes modulo `d`,

\[
A_{m,d}(r)
:=\sum_{\substack{0\le j<m\\j\equiv r\pmod d}}a_m(j),
\qquad 0\le r<d.
\tag{13}
\]

CRT counting over one period `lcm(m,n)` gives

\[
\boxed{
\gamma_{m,n}
=\frac{d}{\sqrt{mnh_mh_n}}
\sum_{r=0}^{d-1}A_{m,d}(r)A_{n,d}(r).
}
\tag{14}
\]

If `omega_d=e^{2pi i/d}`, finite Fourier inversion converts (14) into

\[
\boxed{
\gamma_{m,n}
=\frac{1}{\sqrt{mnh_mh_n}}
\sum_{t=0}^{d-1}
\Phi_m(\omega_d^t)
\overline{\Phi_n(\omega_d^t)}.
}
\tag{15}
\]

Thus even after different levels are compared inside one refined fiber, their complete pairwise linear geometry is still a finite packet of classical cyclotomic values at roots of unity.

A particularly strong consequence occurs when `(m,n)=1`. Then `d=1`, so (15) reduces to

\[
\boxed{
\gamma_{m,n}=c_mc_n
\qquad((m,n)=1).
}
\tag{16}
\]

Therefore, after centering

\[
\widetilde g_n:=g_n-c_n\mathbf1,
\tag{17}
\]

we have the exact coprime-flatness law

\[
\boxed{
\langle\widetilde g_m,\widetilde g_n\rangle=0
\qquad((m,n)=1).
}
\tag{18}
\]

The first connected Hilbert coupling between two common-refinement primitive masks is supported only on conductors sharing a nontrivial divisor. In particular, this scalar mask geometry supplies no irreducible off-diagonal coupling between distinct prime directions.

## 4. The own exact-order Fourier sector vanishes identically

PC-066 identifies

\[
\widehat{\widehat{\mathbb Z}}\cong\mathbb Q/\mathbb Z
\]

and the exact-order projector `P_d` onto characters of conductor/order `d`; its kernel is the classical Ramanujan sum `c_d`.

Because `g_n` factors through `Z/nZ`, its Fourier support contains only characters whose order divides `n`. For `d|n` and `(a,d)=1`, direct finite Fourier transform of (8) gives

\[
\boxed{
\widehat g_n(a/d)
=\frac{\Phi_n(e^{-2\pi ia/d})}{\sqrt{nh_n}}.
}
\tag{19}
\]

If `d=n`, the root `e^{-2pi ia/n}` is primitive of exact order `n`, hence it is a zero of `Phi_n`. Therefore

\[
\boxed{
P_ng_n=0
\qquad(n>1).
}
\tag{20}
\]

This is the sharpest obstruction in the common-refinement realization. The vector built from the **primitive `n`-th cyclotomic polynomial** has no Fourier mass at all in the **new/exact-order `n` transverse sector**. Every nonzero Fourier component of `g_n` lies on a proper-divisor conductor.

Equivalently,

\[
\boxed{
g_n\in\bigoplus_{d|n,\ d<n}E_d,}
\tag{21}
\]

with the notation `E_d=Ran(P_d)` from PC-066. The primitive shell survives only through its coefficient pattern evaluated on older character sectors; the most literal attempt to turn that mask into a new-conductor fiber state annihilates the new sector by the defining root property of `Phi_n` itself.

For a prime `p`, the statement is total. Since

\[
\Phi_p(z)=S_p(z),
\qquad
h_p=p,
\]

we obtain

\[
\boxed{g_p=\mathbf1.}
\tag{22}
\]

Thus **all prime levels become exactly the same vector** in the canonical common-refinement coefficient Hilbert space. The prime label is absent from the normalized state; only the already-classical unnormalized scale can remember `p`.

## 5. Prime powers are independent `p`-adic Haar/valuation chains

The prime-power sector can be classified completely. For `r>=1`,

\[
\Phi_{p^r}(z)
=1+z^{p^{r-1}}+\cdots+z^{(p-1)p^{r-1}},
\qquad
h_{p^r}=p.
\tag{23}
\]

Hence (8) becomes

\[
\boxed{
g_{p^r}(x)
=p^{(r-1)/2}\,
\mathbf1_{p^{r-1}\widehat{\mathbb Z}}(x).
}
\tag{24}
\]

Put

\[
u_{p,j}:=g_{p^{j+1}}
=p^{j/2}\mathbf1_{p^j\widehat{\mathbb Z}},
\qquad j\ge0.
\tag{25}
\]

Then `u_{p,0}=1` and normalized Haar counting gives

\[
\boxed{
\langle u_{p,j},u_{p,k}\rangle
=p^{-|j-k|/2}.
}
\tag{26}
\]

For distinct primes `p!=q`, CRT independence gives

\[
\boxed{
\langle u_{p,j},u_{q,k}\rangle
=p^{-j/2}q^{-k/2}
=\langle u_{p,j},\mathbf1\rangle
 \langle\mathbf1,u_{q,k}\rangle.
}
\tag{27}
\]

Thus the centered prime-power chains for distinct primes are exactly orthogonal. Within one prime chain define, for `j>=1`,

\[
\psi_{p,j}
:=\frac{u_{p,j}-p^{-1/2}u_{p,j-1}}
{\sqrt{1-p^{-1}}}.
\tag{28}
\]

Equations (26)--(27) give

\[
\boxed{
\{\mathbf1\}\cup
\{\psi_{p,j}:p\text{ prime},\ j\ge1\}
\text{ is an orthonormal family.}
}
\tag{29}
\]

This is precisely the elementary martingale/Haar orthogonalization of nested `p`-adic divisibility cylinders. Consequently the entire Mangoldt-supported prime-power coefficient sector contains one common constant mode plus independent prime-local valuation chains; there is no source-forced mixed-prime Hilbert coupling left to discover in this realization.

## 6. Controls and failure boundary

Several controls prevent overinterpreting the result.

First, (20) is **not prime-specific**. It holds for every `n>1`, including matched composite controls, because it is ultimately the defining statement that primitive `n`-th roots are zeros of `Phi_n`. Therefore the vanishing of the exact-order sector cannot itself be promoted to a primality or RH criterion.

Second, nontrivial shared-factor correlations do survive. For example the scalar `gamma_{m,n}` can be nonzero, and even signed, when `(m,n)>1`; equation (15) records those correlations exactly. The theorem does not claim that all common-refinement coefficient fields are mutually independent.

Third, mixed-composite masks can have genuinely nonconstant old-conductor profiles. Equations (20)--(21) say where their Fourier mass is allowed to live, not that it vanishes. A nonlinear operation on several such profiles, an incidence tensor that is not reduced to pairwise mask Gram data, or a construction retaining vertex/root positions rather than coefficient masks is outside this result.

Finally, the direct-limit identification is specific to the **universal Haar refinement** selected by PC-210. A different matrix-valued/non-Haar fiber transport is not classified here and would need its own geometric derivation and novelty audit.

## 7. Prior-art and novelty audit

The abstract ingredients are established mathematics.

The fact that `hat Z` is the inverse limit of the finite cyclic groups and has Pontryagin dual `Q/Z` is standard compact-abelian/profinite harmonic analysis; PC-064--PC-066 already record this structure for Prime Circle. The exact-order character projectors and their Ramanujan kernels are already classicalized in PC-066.

The filter-mask/common-refinement viewpoint is standard wavelet and Cuntz-representation territory. Ola Bratteli, David E. Evans, and Palle E. T. Jorgensen, *Compactly supported wavelets and representations of the Cuntz relations*, Applied and Computational Harmonic Analysis 8 (2000), 166--196, DOI `10.1006/acha.2000.0283`, is a direct prior-art anchor for finite masks and Cuntz isometries. Joachim Cuntz and Anatoly Vershik, *C*-Algebras Associated with Endomorphisms and Polymorphisms of Compact Abelian Groups*, Communications in Mathematical Physics 321 (2013), 157--179, DOI `10.1007/s00220-012-1647-0`, supplies neighboring operator-algebra context for endomorphisms of compact abelian groups.

Most importantly, finite Fourier evaluation of cyclotomic polynomials at roots of unity is established arithmetic. Bartlomiej Bzdega, Andres Herrera-Poyatos, and Pieter Moree, *Cyclotomic polynomials at roots of unity*, Acta Arithmetica 184 (2018), 215--230, DOI `10.4064/aa170112-20-12`, explicitly studies `Phi_n` at nonprimitive roots using finite Fourier analysis; vanishing at primitive `n`-th roots is of course the defining cyclotomic property. The prime-power cylinder functions in (24) and the orthogonalization (28) are elementary `p`-adic Haar/martingale structure, neighboring the standard `p`-adic wavelet theory of S. V. Kozyrev, *Wavelet theory as p-adic spectral analysis*, Izvestiya: Mathematics 66 (2002), 367--376, DOI `10.1070/IM2002V066N02ABEH000381`.

No novelty is claimed for profinite Fourier analysis, Cuntz/filter masks, cyclotomic root evaluations, or `p`-adic Haar functions. The durable contribution is the **Prime-Circle-specific exact boundary** obtained when those classical pieces are composed: the canonical Haar common-refinement lift of the direct primitive weighted covers has a central pairwise Gram geometry, its connected coprime couplings vanish, and each `Phi_n` coefficient state is annihilated by its own exact-order projector.

## 8. RH consequence and surviving frontier

The result removes a natural interpretation of the PC-211 escape. Merely comparing different direct primitive covering degrees after carrying them to a common universal refinement does not reveal a new operator-valued prime interaction. At the pairwise level one obtains only the scalar kernel (15); for coprime conductors its connected part is exactly zero, and on the prime-power/Mangoldt support the nonconstant sector splits into independent `p`-adic Haar chains.

Nothing here supplies a spectral parameter `s`, an archimedean gamma factor, a functional equation, or a critical-line selector. Introducing weights in the exact-order decomposition would return to the arbitrary conductor scale already exposed by PC-066; Dirichlet/Mellin summation over the anchored scalar would return to the classical Mangoldt transforms excluded by the research mandate.

What remains outside the theorem is narrower and concrete: old/new incidence operators that retain more than coefficient masks, matrix-valued or non-Haar fiber sectors, genuinely nonlinear couplings among mixed-composite cylinder fields, growing tensor/relation modules whose state is not determined by pairwise Gram data, or global uniformization/monodromy. In particular, any continuation of the preimage/fiber-sector direction must preserve a non-scalar sector **before** the universal common-refinement mask gauge reduces it to `L^2(hat Z)` cylinder geometry.
