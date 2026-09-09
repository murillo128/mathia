# PC-228 — repeated-prime depth aliases fresh-prime transfer through the squarefree radical

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the repeated-prime part of the simultaneous-base-growth escape left open by PC-226--PC-227. For the source-derived fresh-prime transfer of PC-224/PC-227, every repeated prime exponent in the coarse conductor factors out exactly before any mode-resolved new-prime information is created. The full transfer at coarse level `N` is a deterministic support dilation and Fourier aliasing of the transfer at `rad(N)`, preceded by a coisometric collapse of source unit modes along reduction `U(N) -> U(rad(N))`.

Consequently repeated-prime depth cannot enlarge the nonzero packet state of this architecture. If `s=N/rad(N)`, the nonzero squared singular values at level `N` are exactly `s` times those at the squarefree radical level, while the additional `phi(N)-phi(rad(N))` source directions enter only through a forced kernel. In particular, along a prime-power base `N=p^a` the transfer has only `p-1` nonzero singular directions for every `a`; growing `a` makes the source rank fraction `p^{1-a}` rather than creating new spectral degrees of freedom.

This does **not** close growth of the squarefree radical, nor does it close a later source-forced operation that resolves the deterministic alias labels created by the dilation. It closes the simpler possibility that repeated-prime conductor depth itself supplies new mode-resolved amplitude data to the one-mask fresh-prime transfer.

## 1. The source transfer and the radical decomposition

Let `N>1`, put

\[
R=\operatorname{rad}(N),
\qquad
s=\frac NR,
\]

and let `q` be a prime with `q\nmid N`. Write

\[
M=Nq=sRq.
\]

Use the normalized finite Hilbert spaces

\[
H_m=L^2(\mathbb Z/m\mathbb Z)
\]

with normalized counting measure. For `a|b`, let

\[
J_{a,b}:H_a\to H_b
\]

be the canonical pullback along reduction modulo `a`. Let `E_q^{(N)}` denote the PC-224 conditional-expectation projection from `H_M` onto the old subspace `J_{N,M}H_N`.

Let

\[
\Phi_M(z)=\sum_{x=0}^{M-1}a_M(x)z^x,
\qquad
h_M=\sum_x a_M(x)^2,
\]

with zero padding beyond the degree, and use the normalized cyclotomic coefficient mask

\[
g_M(x)=\sqrt{\frac{M}{h_M}}\,a_M(x).
\]

Finally let `\mathscr E_N` be the exact-order-`N` Fourier sector, with orthonormal basis

\[
e_u^{(N)}(x)=e^{2\pi iux/N},
\qquad u\in U(N).
\]

The mode-resolved fresh-prime transfer studied in PC-227 is

\[
\boxed{
T_{N,q}
:=
(I-E_q^{(N)})M_{g_M}J_{N,M}\big|_{\mathscr E_N}.
}
\tag{1}
\]

PC-227 analyzes this operator by its exact target Fourier amplitudes. The question here is whether repeated prime powers inside the **coarse** level `N` can make this full transfer richer when `N` itself grows.

## 2. The cyclotomic mask is an exact radical dilation

The classical radical identity for cyclotomic polynomials is

\[
\boxed{
\Phi_n(z)
=
\Phi_{\operatorname{rad}(n)}
\!\left(z^{n/\operatorname{rad}(n)}\right),
\qquad n>1.
}
\tag{2}
\]

It follows either by iterating `Phi_{pn}(z)=Phi_n(z^p)` when `p|n`, or directly from the Möbius product. Since `rad(M)=Rq` and `M/rad(M)=s`, equation (2) gives

\[
\boxed{
\Phi_M(z)=\Phi_{Rq}(z^s).
}
\tag{3}
\]

Therefore

\[
a_M(x)=0\quad(s\nmid x),
\qquad
a_M(sc)=a_{Rq}(c),
\tag{4}
\]

and in particular

\[
\boxed{h_M=h_{Rq}.}
\tag{5}
\]

Define the support-dilation isometry

\[
I_s:H_{Rq}\to H_M
\]

by

\[
\boxed{
(I_sF)(x)
=
\begin{cases}
\sqrt s\,F(c),&x=sc,\\
0,&s\nmid x.
\end{cases}}
\tag{6}
\]

Normalized counting makes (6) an isometry exactly. Equations (3)--(5) then say that the fine coefficient mask itself is only the radical mask embedded on the subgroup of multiples of `s`:

\[
\boxed{
g_M(sc)=\sqrt s\,g_{Rq}(c),
\qquad g_M(x)=0\ (s\nmid x).}
\tag{7}
\]

Thus repeated-prime depth has already become a deterministic position-space dilation before the old/new projection is applied.

## 3. Source exact-order modes collapse along `U(N) -> U(R)`

Reduction modulo `R` gives a surjection

\[
\pi:U(N)\twoheadrightarrow U(R).
\tag{8}
\]

Prime-power CRT counting gives

\[
|U(N)|=\varphi(N)=s\varphi(R),
\]

so every fiber of (8) has exactly `s` elements.

Define

\[
D_s:\mathscr E_N\to\mathscr E_R
\]

on the Fourier basis by

\[
D_se_u^{(N)}=e_{\pi(u)}^{(R)}.
\tag{9}
\]

Then

\[
D_sD_s^*=sI_{\mathscr E_R}.
\]

It is convenient to normalize this to the coisometry

\[
\boxed{C_s=s^{-1/2}D_s,\qquad C_sC_s^*=I_{\mathscr E_R}.}
\tag{10}
\]

Now take a source basis vector `e_u^(N)` and evaluate its canonical lift on the support of the mask. At `x=sc`,

\[
(J_{N,M}e_u^{(N)})(sc)
=e^{2\pi iuc/R}
=(J_{R,Rq}e_{\pi(u)}^{(R)})(c).
\tag{11}
\]

Combining (7) and (11) proves the exact pre-projection operator identity

\[
\boxed{
M_{g_M}J_{N,M}\big|_{\mathscr E_N}
=I_sM_{g_{Rq}}J_{R,Rq}D_s
=\sqrt s\,I_sM_{g_{Rq}}J_{R,Rq}C_s.
}
\tag{12}
\]

All source modes that differ only inside one reduction fiber of `U(N)->U(R)` therefore produce the same masked fine vector before the new-prime projection.

## 4. Conditional expectation respects the same dilation

The PC-224 old projection averages over the `q` lifts of a coarse residue. If `x=sc` is a multiple of `s`, its `q` lifts modulo `M` are

\[
sc+tN=s(c+tR),
\qquad0\le t<q,
\]

which are precisely the support-dilated lifts of `c` modulo `Rq`. If `s\nmid x`, adding `N=sR` never changes that residue class modulo `s`, so the whole old fiber remains outside the support of `I_s`.

Hence the conditional expectations intertwine exactly:

\[
\boxed{
E_q^{(N)}I_s
=I_sE_q^{(R)}.
}
\tag{13}
\]

Subtracting from the identity and using (12) gives the main factorization:

\[
\boxed{
T_{N,q}
=I_sT_{R,q}D_s
=\sqrt s\,I_sT_{R,q}C_s.
}
\tag{14}
\]

Equation (14) is an equality of the complete source-to-new-prime operators. No singular-value contraction, asymptotic limit, or target Fourier summation has been taken.

## 5. The entire nonzero singular spectrum is radical data

Because `I_s` is an isometry and `C_s` a coisometry, equation (14) gives

\[
\boxed{
T_{N,q}^*T_{N,q}
=s\,C_s^*(T_{R,q}^*T_{R,q})C_s.
}
\tag{15}
\]

The adjoint `C_s^*` is an isometric embedding. Therefore `C_s^*BC_s` is unitarily equivalent to `B` on `Ran(C_s^*)` and is zero on its orthogonal complement. Consequently

\[
\boxed{
\operatorname{Spec}^{\times}(T_{N,q}^*T_{N,q})
=s\,\operatorname{Spec}^{\times}(T_{R,q}^*T_{R,q}),
}
\tag{16}
\]

including multiplicities, and

\[
\boxed{
\operatorname{rank}T_{N,q}
=
\operatorname{rank}T_{R,q}.
}
\tag{17}
\]

The kernel dimension is therefore

\[
\boxed{
\dim\ker T_{N,q}
=(s-1)\varphi(R)+\dim\ker T_{R,q}.
}
\tag{18}
\]

This is the exact information statement relevant to the current frontier. Repeated-prime depth can rescale existing nonzero singular values, but it cannot add even one new nonzero singular direction. For fixed squarefree radical `R`, the rank stays bounded as all prime exponents of `N` grow.

## 6. Mode resolution is only deterministic Fourier aliasing

The conclusion is not an artifact of passing to `T^*T`. Equation (14) retains the full output vector. Its only extra target structure is the Fourier image of the support dilation (6).

Let `L=Rq`. For every `F in H_L`, normalized finite Fourier transform gives

\[
\boxed{
\widehat{I_sF}(k)
=s^{-1/2}\widehat F(k\bmod L),
\qquad k\bmod sL.
}
\tag{19}
\]

Thus each radical-level target mode is copied into exactly `s` equal-amplitude aliases

\[
k_0,\ k_0+L,\ \ldots,\ k_0+(s-1)L.
\tag{20}
\]

Because `q|L`, a radical mode with nonzero new `q` coordinate remains a new-`q` mode in every alias. There is no extra amplitude packet hidden in the repeated prime powers: the complete fine Fourier vector is determined by the radical transfer plus the universal alias map (19).

The aliases can have different **exact conductor labels** with respect to primes already dividing `N`. A later exact-order-sensitive source operator could therefore act differently on them. That is a genuine boundary of the theorem, not a contradiction: such an operator would use additional structure after the deterministic embedding. Equation (14) says only that the one-mask fresh-prime transfer itself creates no new repeated-depth amplitudes.

## 7. Prime-power bases become finite-rank replicated columns

Take

\[
N=p^a,
\qquad R=p,
\qquad s=p^{a-1},
\qquad q\ne p.
\]

PC-227 proves that the prime-base transfer is exactly flat on its source sector:

\[
T_{p,q}^*T_{p,q}=\lambda_{p,q}I_{\mathscr E_p},
\tag{21}
\]

with `lambda_{p,q}>0` given there by the finite sine-ratio sum. Equation (15) now gives

\[
\boxed{
T_{p^a,q}^*T_{p^a,q}
=s\lambda_{p,q}\Pi_{p^a\to p},
}
\tag{22}
\]

where

\[
\Pi_{p^a\to p}:=C_s^*C_s
\]

is the orthogonal projection onto source vectors constant on the `s`-element reduction fibers `U(p^a)->U(p)`.

Therefore

\[
\boxed{
\operatorname{rank}T_{p^a,q}=p-1,
\qquad
\dim\ker T_{p^a,q}=(p-1)(p^{a-1}-1),
}
\tag{23}
\]

and the `p-1` nonzero squared singular values are all

\[
\boxed{p^{a-1}\lambda_{p,q}.}
\tag{24}
\]

The source rank fraction is exactly

\[
\boxed{
\frac{p-1}{\varphi(p^a)}=p^{1-a}.
}
\tag{25}
\]

So the repeated-depth direction of simultaneous base growth becomes asymptotically almost entirely null.

A small exact control makes the replication visible. For `p=2,q=3`, PC-227's formula gives

\[
\lambda_{2,3}=\frac49.
\]

At `N=4`, the two source units reduce to the same unit modulo `2`, so

\[
T_{4,3}^*T_{4,3}
=\frac49
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

with eigenvalues `8/9,0`. At `N=8` the four source columns are the same reduction copy and the Gram matrix is `(4/9)J_4`, with eigenvalues `16/9,0,0,0`. These are exactly the `s=2` and `s=4` instances of (22)--(24), not numerical approximations.

## 8. Prior-art and novelty audit

The arithmetic input is classical. The radical substitution (2) is a standard cyclotomic identity and follows immediately from the Möbius product; the existing Carlo Sanna survey in `research/prime_circle/SOURCES.md` is the line's broad modern anchor for cyclotomic coefficient structure. A directed literature check also finds the identity stated explicitly in standard cyclotomic coefficient references/databases. No novelty is claimed for coefficient dilation under (2), for reduction of unit groups, or for the Fourier aliasing formula (19), which is ordinary finite cyclic Fourier analysis.

The project-specific content is the exact operator factorization (14) for the **particular source-derived PC-224--PC-227 fresh-prime transfer**, and its consequences (16)--(25). A directed search around the radical cyclotomic identity, coefficient dilation, finite-cyclic Fourier aliasing, and fresh-prime refinement did not expose an independent zeta/RH mechanism or a literature formulation that changes the classification. This result should therefore be read as a research-boundary theorem, not as a historically novel theorem about cyclotomic polynomials.

The comparison with earlier Prime-Circle boundaries is also important. PC-078 found a radical tensor inflation for a different Hardy/Hilbert operator, and PC-212/PC-213 found prime-local radical behavior for common-refinement coefficient masks and prime-power support incidence. Those results make radical collapse a strong matched control rather than evidence by itself. PC-228 shows that the same control reaches the **current mode-resolved fresh-prime transfer** and closes precisely the repeated-prime part of the new simultaneous-growth escape left by PC-227.

## 9. Falsification boundary and surviving route

The theorem can be falsified directly at three independent points:

- a coefficient of `Phi_{Nq}` outside a multiple of `s=N/rad(N)` would contradict (3)--(4);
- a source unit pair with the same reduction in `U(R)` producing different masked new-prime vectors would contradict (11)--(14);
- any nonzero squared singular value of `T_{N,q}` not equal to `s` times a radical-level value would contradict (15)--(16).

The exact small controls above and the symbolic derivation agree with all three tests.

The result does **not** cover a source operation inserted before the cyclotomic mask that resolves the fibers of `U(N)->U(R)`, an exact-order projector or other noncommuting operator inserted after the alias map and before contraction, multiple masks separated by such operations, a fresh-prime step with `q|N`, or simultaneous growth in which the squarefree radical `R` itself gains new primes. Those mechanisms contain data absent from the one-mask factorization and require separate derivation and novelty audit.

## Research consequence

PC-226 and PC-227 showed that a fixed coarse base has only finite fresh-prime residue/Cauchy packet limits, while leaving simultaneous base growth as a genuine escape. PC-228 removes one large part of that escape exactly:

\[
\boxed{
\text{growing repeated-prime exponents at fixed radical}
\quad\Longrightarrow\quad
\text{same radical transfer + deterministic aliases + forced source kernel}.
}
\]

Hence **only growth of the squarefree radical can enlarge the source-derived mode-resolved state in this architecture**. Repeated-prime depth can change scales and exact-order labels available to a later operator, but it does not itself supply new fresh-prime transfer amplitudes or new nonzero singular directions.