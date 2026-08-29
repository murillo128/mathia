# PC-052 — a new-prime cotangent two-shell union is affine base inflation

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the most direct **simultaneous fine+coarse cotangent spectrum** under one genuinely new prime refinement. If `p` is a prime with `p\nmid d`, the complete `p`-fold preimage tube over the primitive shell `P_d^*` is exactly the two-shell union `P_d^*\sqcup P_{dp}^*`. Keeping both shells and all intrinsic cotangent couplings between them does not create a new scale spectrum: after Fourier transform along the `p` lifts, the whole joint operator splits into explicit affine copies of the base-level primitive cotangent operator plus the universal rank-one matrix `J`. Equivalently, the augmented characteristic polynomial is an exact product of affine rescalings of one base polynomial.

This closes the immediate escape left by PC-049/PC-050 in which one refuses to fiber-average and instead keeps **both** the coarse primitive shell, the fine primitive shell, and their rectangular old/new coupling in one natural spectral operator. It also complements PC-051: when `p\mid d`, the same `p`-fold tube consists only of the repeated-prime fine shell and gives the affine ladder proved there; when `p\nmid d`, the tube splits into the coarse and new fine shells, but the full joint spectrum obeys the same universal lift law.

The result does **not** rule out a principal compression to the fine shell followed by additional nonlinear processing, rectangular Gram/dilation constructions spanning several unrelated levels, Lewis–Zagier-type asymptotic determinant spaces, shell-dependent kernels, or the global uniformization/monodromy direction of PC-017.

## 1. The intrinsic `p`-preimage tube is exactly two birth shells

Let

\[
U(d)=(\mathbb Z/d\mathbb Z)^\times,
\qquad p\nmid d.
\]

Inside the `dp`-gon consider all `p` lifts of every primitive `d`-residue,

\[
Y_{d,p}
:=\{a+dt\pmod{dp}:a\in U(d),\ t\in\mathbb Z/p\mathbb Z\}.
\]

Equivalently,

\[
Y_{d,p}
=\{x\pmod{dp}:\gcd(x,d)=1\}.
\]

If the residue of `x` modulo `p` is nonzero, then `x\in U(dp)` and the corresponding root has exact order `dp`. If `x\equiv0\pmod p`, write `x=pc`; then `c\in U(d)` and

\[
\zeta_{dp}^{x}=\zeta_d^c
\]

has exact order `d`. Therefore, as a set of points on the original circle,

\[
\boxed{
Y_{d,p}\quad\longleftrightarrow\quad P_d^*\sqcup P_{dp}^*.
}
\]

This is not an auxiliary completion: it is precisely the full inverse image of `P_d^*` under the intrinsic power map

\[
z\longmapsto z^p.
\]

Each coarse primitive vertex has exactly `p` preimages; one remains in the old shell `P_d^*` and the other `p-1` are born in `P_{dp}^*`.

## 2. The full joint cotangent operator is fiber-circulant

Use the canonical oriented cotangent kernel from PC-045,

\[
H_N^{\rm full}(x,y)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(x-y)}N\right),&x\ne y,\\[2mm]
0,&x=y.
\end{cases}
\]

Restrict it to the complete lift tube:

\[
\boxed{
C_{d,p}:=H_{dp}^{\rm full}[Y_{d,p},Y_{d,p}].
}
\]

In the lift coordinates `(a,t)` above,

\[
C_{d,p}((a,t),(b,u))
=
i\cot\!\left(
\frac{\pi((a-b)+d(t-u))}{dp}
\right)
\]

away from the identical fine vertex, where the diagonal is zero. Hence the fiber variables occur only through `t-u`. Translation

\[
(t,u)\mapsto(t+1,u+1)
\]

is an exact symmetry, so finite Fourier transform in the fiber coordinate block-diagonalizes the **entire two-shell operator before either shell is discarded**.

In the shell ordering `P_{dp}^*\sqcup P_d^*`, the same matrix has the form

\[
\boxed{
C_{d,p}\simeq
\begin{pmatrix}
H_{dp} & B_{dp,d}\\
B_{dp,d}^* & H_d
\end{pmatrix},
}
\]

up to the harmless multiplicative permutation identifying the embedded order-`d` residues with `U(d)`. Thus `C_{d,p}` retains the fine block, the coarse block, and exactly the old/new shell coupling classified coefficientwise in PC-048.

## 3. Exact fiber Fourier blocks

Let

\[
\omega=e^{2\pi i/p}
\]

and Fourier transform the fiber coordinate by the characters `t\mapsto\omega^{jt}`. Put

\[
H_d:=H_d^{\rm full}[U(d),U(d)],
\qquad
A_d:=H_d+J_d,
\]

where `J_d` is the all-ones matrix on `U(d)`. For `0\le j<p`, define the diagonal unitary

\[
D_j(a,a)=
\exp\!\left(\frac{2\pi ija}{dp}\right),
\qquad D_0=I.
\]

Fix `\delta=a-b`. For `\delta\not\equiv0\pmod d`, the `j`-th fiber coefficient is

\[
S_j(\delta)
=\sum_{r=0}^{p-1}
\omega^{-jr}
 i\cot\!\left(
\frac{\pi(\delta+dr)}{dp}
\right).
\]

For `j=0`, the classical cotangent multiplication formula gives

\[
\boxed{
S_0(\delta)=p\,i\cot\!\left(\frac{\pi\delta}{d}\right).
}
\]

For `1\le j<p`, write

\[
q=e^{2\pi i\delta/(dp)}.
\]

Using

\[
i\cot\theta=\frac{1+e^{2i\theta}}{1-e^{2i\theta}}
\]

and the finite root-of-unity identity

\[
\sum_{r=0}^{p-1}
\frac{\omega^{-kr}}{1-q\omega^r}
=\frac{pq^k}{1-q^p},
\qquad 0\le k<p,
\]

one gets

\[
\boxed{
S_j(\delta)
=
\frac{2pq^j}{1-q^p}
=
pq^j
\left(
1+i\cot\!\frac{\pi\delta}{d}
\right).
}
\]

For `\delta=0`, the removed singular term is exactly the zero diagonal of `C_{d,p}` and the standard finite cotangent transform gives

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

Therefore the fiber Fourier blocks are exactly

\[
\boxed{K_0=pH_d}
\]

and, for `1\le j<p`,

\[
\boxed{
K_j
=
pD_jA_dD_j^{-1}-2jI.
}
\]

No arithmetic or spectral approximation is used: this is an entrywise finite identity.

## 4. The full two-shell spectrum contains only affine base copies

The previous decomposition immediately gives the unaugmented spectrum

\[
\boxed{
\operatorname{Spec}(C_{d,p})
=
p\operatorname{Spec}(H_d)
\;\sqcup\;
\bigsqcup_{j=1}^{p-1}
\left(p\operatorname{Spec}(A_d)-2j\right).
}
\]

Thus the entire joint spectral problem on

\[
P_d^*\sqcup P_{dp}^*
\]

is determined by the two base-level matrices `H_d` and `A_d=H_d+J_d`. The new prime contributes only the universal scale `p`, the universal integer shifts `-2j`, and known diagonal conjugations that disappear from the spectrum.

The rank-one augmentation makes the closure even cleaner. Let

\[
\mathcal A_{d,p}:=C_{d,p}+J_{Y_{d,p}}.
\]

Since `J_{Y_{d,p}}=J_d\otimes J_p` in lift coordinates, its fiber Fourier transform contributes only `pJ_d` to the constant mode. Hence **all** fiber blocks take the same affine form:

\[
\boxed{
\mathcal A_{d,p}
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
\operatorname{Spec}(\mathcal A_{d,p})
=
\bigsqcup_{j=0}^{p-1}
\left(p\operatorname{Spec}(A_d)-2j\right).
}
\]

If `m=\varphi(d)` and

\[
\chi_d(z)=\det(zI-A_d),
\]

then the complete augmented characteristic polynomial is

\[
\boxed{
\det(zI-\mathcal A_{d,p})
=
p^{mp}
\prod_{j=0}^{p-1}
\chi_d\!\left(\frac{z+2j}{p}\right).
}
\]

The unaugmented polynomial similarly factors as

\[
\boxed{
\det(zI-C_{d,p})
=
p^{mp}
\det\!\left(\frac zp I-H_d\right)
\prod_{j=1}^{p-1}
\chi_d\!\left(\frac{z+2j}{p}\right).
}
\]

Thus keeping the complete fine/coarse coupling does not produce a new determinant whose zeros depend on an unexplained arithmetic scale interaction. It produces an explicit finite affine inflation of base-level zeros.

## 5. Relation to PC-048/049/050/051

This identity organizes several previously separate boundaries.

- **PC-048:** the rectangular block `B_{dp,d}` can have large rank and its character coefficients are nontrivial fixed `L(0)` / Bernoulli data. PC-052 shows that, when this block is assembled with both endpoint shell operators into the canonical two-shell cotangent matrix, the **joint spectrum** is nevertheless an affine base inflation. Large cross-block rank does not imply a new joint spectral family.
- **PC-049:** summing the fine fibers gives a commuting invertible coarse pushforward. PC-052 instead keeps all `p` lift coordinates and diagonalizes them exactly; the coarse pushforward is only one projection of this more complete fiber-circulant structure.
- **PC-050:** averaging forgets repeated-prime depth. PC-052 shows that the genuinely new-prime two-shell tube also has an exact finite lift law before averaging.
- **PC-051:** if `p\mid d`, all `p` lifts of a primitive `d`-root are primitive at level `dp`, so the same lift-tube calculation acts directly on `P_{dp}^*` and yields the repeated-prime affine ladder. If `p\nmid d`, exactly one lift remains in `P_d^*`; retaining it restores the full cyclic fiber and produces the two-shell decomposition above.

So the missing zero residue in the new-prime primitive fiber is precisely the **coarse old vertex**. Once that geometrically forced old vertex is retained, the apparently broken cyclic fiber becomes complete again and the operator closes over base data.

## 6. Prior-art and novelty audit

The analytic ingredients are classical and already anchored in `research/prime_circle/SOURCES.md`.

- Finite Fourier diagonalization of block-circulant matrices is standard.
- The cotangent multiplication/distribution identity is classical and underlies Petersson–Knopp-type scale identities; Beck's *Dedekind cotangent sums* and Parson's *Dedekind sums and Hecke operators* are the relevant scale-law boundary already used in PC-049/050.
- Ejsmont–Lehner's *The Trace Method for Cotangent Sums* is a direct finite-matrix prior-art boundary for interpreting affine cotangent spectra as a novel spectral phenomenon.
- Lewis–Zagier's GRH criterion uses a substantially different multi-scale Gram/dilation construction and asymptotic determinant problem. Their result is evidence that cotangent data can be RH-relevant when the scale coupling is genuinely different; it is not contradicted by this finite preimage-tube factorization.

Directed searches across cotangent distribution identities, block-circulant cotangent matrices, Petersson–Knopp/Hecke scaling, and cotangent GRH criteria did not locate this exact primitive-root **two-shell preimage-tube** formulation. That absence is not evidence of historical priority. No novelty claim is made for the Fourier, cotangent, or determinant ingredients.

The durable prime-circle consequence is the obstruction specific to its birth geometry:

\[
\boxed{
\text{for a new prime }p,\ 
P_d^*\sqcup P_{dp}^*
\text{ restores a complete }p\text{-fiber whose cotangent spectrum is affine base data.}
}
\]

## 7. Consequence for the RH search

A natural response to the information loss in canonical fiber averaging is to keep the coarse shell, the fine shell, and their coupling simultaneously and ask whether the joint matrix spectrum contains the missing scale interaction. For the intrinsic cotangent kernel, PC-052 rules out that route:

\[
\boxed{
P_d^*\sqcup P_{dp}^*
\to
\text{full cotangent fine/coarse operator}
\to
\text{joint spectral determinant}
\to
\text{new RH mechanism}
}
\]

fails under the stated construction. The determinant has no new complex parameter `s`, no gamma completion, no intrinsic `s\leftrightarrow1-s` functional symmetry, and no mechanism selecting `\operatorname{Re}s=1/2`. The new prime enters only through an elementary affine replication of base-level finite spectra.

The boundary remains important. This finding does **not** rule out:

- deleting the coarse shell and then using information in the resulting principal compression together with another level-dependent structure;
- rectangular Gram operators coupling **several** levels with nontrivial dilation weights rather than the canonical cotangent matrix on one preimage tube;
- Lewis–Zagier/Nyman–Beurling-type asymptotic scale spaces;
- nonlinear operations that mix distinct fiber Fourier sectors after the canonical operator is formed;
- shell-dependent deformations carrying an independently derived parameter;
- or the global primitive-root uniformization/monodromy defect of PC-017.

The practical restriction is sharper than “do not average”: **even retaining the complete adjacent coarse+fine cotangent system is spectrally universal once it is the full power-map preimage tube.** A surviving cotangent route must couple scales in a way that is not reducible to this one-step lift geometry.

## 8. Exact audit tests

The claim is finite-dimensional and has direct falsifiers.

1. Verify set-theoretically for `p\nmid d` that
   \[
   Y_{d,p}=U(dp)\sqcup pU(d)
   \]
   and hence that the corresponding roots are `P_{dp}^*\sqcup P_d^*`.
2. Order `Y_{d,p}` by `(a,t)` and verify that the cotangent entries depend on the fiber coordinates only through `t-u`.
3. Fourier transform the fiber coordinate and verify the weighted cotangent sums `S_j(\delta)` above.
4. Check the diagonal transform `0,p-2,p-4,\ldots,2-p`.
5. Recover exactly `K_0=pH_d` and `K_j=pD_j(H_d+J_d)D_j^{-1}-2jI` for `j>0`.
6. Add `J_{Y_{d,p}}` and verify that it changes only the constant fiber block, yielding the uniform affine direct sum.
7. Compare the direct joint spectra and characteristic polynomials with the boxed formulas at small examples such as `(d,p)=(3,5)`, `(5,3)`, and `(6,5)`.

Failure of the two-shell set identity, any fiber Fourier block, or the characteristic-polynomial factorization would invalidate the obstruction. No claim is made that arbitrary multi-level Gram/dilation constructions or nonlinear scale couplings reduce to this affine lift law.