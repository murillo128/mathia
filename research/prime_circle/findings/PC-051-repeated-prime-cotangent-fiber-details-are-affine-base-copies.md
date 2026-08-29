# PC-051 — repeated-prime cotangent fiber details are affine base copies

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for extracting new prime-power-depth spectral information from the **full fine fiber** of the canonical primitive cotangent operator when the refinement prime already divides the coarse level. PC-050 proved that the fiber average is exactly blind to repeated-prime depth. The present result is stronger: before averaging, the repeated-prime lift has an exact fiber Fourier decomposition with **zero coarse/detail mixing**, and every nonconstant fiber block is an explicit unitary-conjugate affine copy of one fixed base operator. Iterating a repeated prime therefore produces only a universal affine spectral ladder over base-level data.

This closes the most immediate fine-fiber escape route left open by PC-050. It does **not** cover a genuinely new prime `p` with `p\nmid d`, simultaneous Gram/dilation constructions retaining several levels, nonlinear operators, or the global uniformization/monodromy direction.

## 1. Repeated-prime fibers carry an exact cyclic translation symmetry

For `N>1`, let

\[
U(N)=(\mathbb Z/N\mathbb Z)^\times
\]

and use the primitive compression of the oriented cotangent kernel from PC-045,

\[
H_N(a,b)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(a-b)}N\right),&a\ne b,\\[2mm]
0,&a=b,
\end{cases}
\qquad a,b\in U(N).
\]

Fix a prime `p|d`. Every primitive residue `a\in U(d)` has exactly `p` unit lifts to `U(dp)`:

\[
(a,t)\longleftrightarrow a+td,
\qquad t\in\mathbb Z/p\mathbb Z.
\]

Thus, after choosing the standard representatives of `U(d)`, there is a canonical fiberwise identification

\[
\mathbb C^{U(dp)}\cong
\mathbb C^{U(d)}\otimes\mathbb C^{\mathbb Z/p\mathbb Z}.
\]

For two lifted vertices,

\[
H_{dp}((a,t),(b,u))
=
i\cot\!\left(
\frac{\pi((a-b)+d(t-u))}{dp}
\right)
\]

except on the identical fine vertex, where the diagonal is defined as zero. The entry depends on the fiber variables only through `t-u`. Therefore simultaneous translation

\[
(t,u)\mapsto(t+1,u+1)
\]

is an exact symmetry of the fine operator.

Let

\[
\omega=e^{2\pi i/p}
\]

and Fourier transform only the fiber coordinate. Then `H_{dp}` becomes block diagonal with `p` blocks `K_j`, `0\le j<p`. In particular,

\[
\boxed{
\text{the fiber-constant sector and every nonconstant fiber mode are exactly decoupled.}
}
\]

So the orthogonal complement of the coarse/fiber-constant space does not interact with it at all in a repeated-prime step.

## 2. Exact weighted cotangent transform on one fiber

Put `\delta=a-b`. For `\delta\not\equiv0\pmod d`, define

\[
q=e^{2\pi i\delta/(dp)}.
\]

Using

\[
i\cot\theta=\frac{1+e^{2i\theta}}{1-e^{2i\theta}},
\]

the `j`-th fiber Fourier coefficient is

\[
S_j(\delta)
=
\sum_{r=0}^{p-1}
\omega^{-jr}
 i\cot\!\left(\frac{\pi(\delta+dr)}{dp}\right).
\]

For the constant mode, the classical cotangent multiplication formula gives

\[
\boxed{
S_0(\delta)
=p\,i\cot\!\left(\frac{\pi\delta}{d}\right).
}
\]

For `1\le j<p`, the finite root-of-unity sum is elementary. Since

\[
\sum_{r=0}^{p-1}
\frac{\omega^{-kr}}{1-q\omega^r}
=
\frac{p q^k}{1-q^p},
\qquad 0\le k<p,
\]

one gets

\[
\boxed{
S_j(\delta)
=
\frac{2p q^j}{1-q^p}
=
p q^j
\left(
1+i\cot\!\frac{\pi\delta}{d}
\right).
}
\]

For `\delta=0`, the removed singular term is precisely the zero diagonal of `H_{dp}`. The remaining finite cotangent transform is the standard cotangent-circulant spectrum:

\[
\boxed{
\sum_{r=1}^{p-1}
\omega^{-jr}i\cot\frac{\pi r}{p}
=
\begin{cases}
0,&j=0,\\
p-2j,&1\le j<p.
\end{cases}
}
\]

No limiting or analytic-continuation argument is involved; these are finite identities.

## 3. Every detail block is an affine copy of one base operator

Let `J_d` be the all-ones matrix on `U(d)` and define the rank-one augmented base operator

\[
\boxed{A_d:=H_d+J_d.}
\]

For `0\le j<p`, let

\[
D_j(a,a)=
\exp\!\left(\frac{2\pi i j a}{dp}\right),
\]

with `D_0=I`. The preceding entrywise identities give

\[
\boxed{K_0=pH_d}
\]

for the coarse/fiber-constant block, while for every detail mode `1\le j<p`,

\[
\boxed{
K_j
=
pD_jA_dD_j^{-1}-2jI.
}
\]

Thus the apparently discarded fine fiber is not an independent operator carrier. Each detail block consists only of:

- the same base matrix `A_d`;
- a known diagonal unitary conjugation `D_j` determined by the lift geometry;
- the universal scale `p`;
- the universal scalar shift `-2j`.

Equivalently,

\[
\boxed{
\operatorname{Spec}(H_{dp})
=
p\operatorname{Spec}(H_d)
\;\sqcup\;
\bigsqcup_{j=1}^{p-1}
\left(p\operatorname{Spec}(A_d)-2j\right),
}
\]

with multiplicities.

This is stronger than the averaging statement of PC-050. There, all detail modes were summed away. Here they are retained completely and classified.

## 4. The augmentation closes exactly under repeated-prime refinement

The use of `A_d=H_d+J_d` is only an algebraic closure device; `J_d` is universal and contains no new arithmetic input. Under the fiber Fourier transform, the all-ones matrix at level `dp` has only a constant-fiber block:

\[
J_{dp}
\longmapsto
\operatorname{diag}(pJ_d,0,\ldots,0).
\]

Therefore the augmented fine operator has the uniform block formula

\[
\boxed{
A_{dp}
\cong
\bigoplus_{j=0}^{p-1}
\left(
 pD_jA_dD_j^{-1}-2jI
\right).
}
\]

Consequently,

\[
\boxed{
\operatorname{Spec}(A_{dp})
=
\bigsqcup_{j=0}^{p-1}
\left(p\operatorname{Spec}(A_d)-2j\right).
}
\]

If `m=\varphi(d)` and

\[
\chi_d(z)=\det(zI-A_d),
\]

then the characteristic polynomial obeys the exact multiplication law

\[
\boxed{
\chi_{dp}(z)
=
p^{mp}
\prod_{j=0}^{p-1}
\chi_d\!\left(\frac{z+2j}{p}\right).
}
\]

Thus even a determinant-level treatment of the entire repeated-prime fine operator contains no new zeros beyond affine rescalings of the base finite spectrum.

## 5. Prime-power depth produces only a universal affine ladder

Because `p|d` remains true at every later step, the previous decomposition iterates without changing form. For every `r\ge1`,

\[
\boxed{
\operatorname{Spec}(A_{dp^r})
=
\left\{
 p^r\lambda-2k:
 \lambda\in\operatorname{Spec}(A_d),
\ 0\le k<p^r
\right\},
}
\]

again with multiplicities inherited from the base spectrum.

Indeed, one repeated-prime step sends

\[
\lambda\mapsto p\lambda-2j,
\qquad 0\le j<p,
\]

and after `r` steps the accumulated shift is

\[
2(j_1p^{r-1}+j_2p^{r-2}+\cdots+j_r),
\]

which runs through exactly `2k`, `0\le k<p^r`.

So increasing the `p`-adic depth does not uncover a progressively richer intrinsic spectrum. It merely replaces each base eigenvalue by a regular affine ladder. The full fine operator remembers the obvious depth through the number and spacing of these copies, but the repeated refinement contributes no new operator coefficients, no new character family, and no new interaction between coarse and detail modes.

This gives a sharper information statement than radical invariance of the average:

\[
\boxed{
\text{repeated-prime fine structure is a deterministic spectral inflation of base-level data.}
}
\]

## 6. Consequence for the RH search

The natural escape route left after PC-050 was to avoid averaging and retain the orthogonal complement of the fiber-constant subspace, hoping that its internal spectrum or its coupling to the coarse sector might carry prime-power depth invisible to the average.

For the canonical oriented cotangent operator, both possibilities fail in a repeated-prime step:

\[
\boxed{
\text{coarse/detail coupling}=0
}
\]

and

\[
\boxed{
\text{every detail spectrum}=p\operatorname{Spec}(A_d)-2j.
}
\]

Hence the chain

\[
\boxed{
\text{repeated-prime primitive refinement}
\to
\text{retain full cotangent fiber details}
\to
\text{new }p\text{-adic depth spectrum}
\to
\text{RH mechanism}
}
\]

is ruled out under this construction. The fine-fiber completion supplies neither a free complex parameter `s`, a gamma completion, an intrinsic `s\leftrightarrow1-s` symmetry, nor a selector for `\operatorname{Re}s=1/2`. Any such structure added after the affine recursion would be external to the repeated-prime cotangent fiber geometry itself.

This does **not** imply that the base operators `H_d` or `A_d` are trivial; it says only that adjoining further powers of a prime already present in `d` introduces no new operator information beyond a universal Fourier/affine replication of that base data.

## 7. Prior-art and novelty audit

The ingredients are classical, and no historical theorem novelty is claimed for them.

- The cotangent multiplication/distribution identity is classical and already anchors PC-049/PC-050.
- Matthias Beck, **Dedekind cotangent sums**, *Acta Arithmetica* 109:2 (2003), 109–130, develops generalized cotangent sums and Petersson–Knopp distribution identities; it is the closest established scale-law boundary already recorded in `SOURCES.md`.
- Wiktor Ejsmont and Franz Lehner, **The Trace Method for Cotangent Sums**, *Journal of Combinatorial Theory, Series A* 177 (2021), Article 105324, realizes cotangent values through finite self-adjoint matrix spectra and is a direct finite-matrix prior-art boundary, also already recorded in `SOURCES.md`.
- Finite Fourier diagonalization of block-circulant matrices is standard linear algebra.

A directed search across cotangent distribution identities, cotangent matrix spectra, finite Fourier transforms, and block-circulant refinements did not locate this exact **primitive repeated-prime fiber decomposition**. Absence of an exact match is not evidence of priority. The durable Mathia contribution is the prime-circle consequence: once the primitive fibers forced by `p|d` are retained rather than averaged, their entire cotangent operator still closes algebraically over the base level and yields only affine spectral copies.

The result is therefore best read as an exact obstruction, not as a claim of a new cotangent theorem.

## 8. Boundaries and exact falsification tests

The hypothesis `p|d` is essential. When `p\nmid d`, the reduction fiber has `p-1` unit lifts rather than the full additive `\mathbb Z/p\mathbb Z` fiber; the missing zero residue breaks the cyclic fiber-translation symmetry used here. PC-049 classifies the coarse pushforward in that case, but the **full new-prime fine fiber** is not covered by this finding.

Also outside the claim are:

- rectangular fine/coarse Gram operators coupling several levels simultaneously rather than one repeated-prime lift;
- Lewis–Zagier-type dilation spaces and determinant asymptotics across a family of scales;
- nonlinear operators that mix fiber Fourier sectors after the canonical cotangent matrix is formed;
- shell-dependent deformations not equal to the intrinsic cotangent kernel;
- and the global primitive-root uniformization/monodromy direction of PC-017.

The exact claim has direct finite falsifiers:

1. order `U(dp)` by base residue `a\in U(d)` and lift coordinate `t\in\mathbb Z/p\mathbb Z`, then verify block-circulance in `t-u`;
2. fiber-Fourier transform and verify that every off-diagonal `j\ne k` block vanishes;
3. for `\delta\ne0`, evaluate the weighted cotangent sum and recover `2pq^j/(1-q^p)`;
4. for `\delta=0`, verify the diagonal values `0,p-2,p-4,\ldots,2-p`;
5. compare each detail block with `pD_j(H_d+J_d)D_j^{-1}-2jI`;
6. verify the augmented characteristic-polynomial multiplication law;
7. iterate two or more repeated-prime steps and check the affine ladder `p^r\lambda-2k`.

Failure of the fiber block diagonalization, any detail-block identity, or the affine spectrum recursion would invalidate the obstruction. No claim is made about the full fine fiber for genuinely new primes or about multi-level constructions that do not reduce to a single repeated-prime cotangent operator.