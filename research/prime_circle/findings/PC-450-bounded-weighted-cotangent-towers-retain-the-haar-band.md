# PC-450 — Bounded weighted cotangent towers retain the Haar band

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + CONTROL-BLIND. For the singleton-base complete cotangent tower, boundedness of the unchanged augmented action on an equivalent weighted space already forces spectrum exactly `[-1,1]`; two-sided boundedness of the density is unnecessary. Classical ergodic weight iteration supplies unbounded densities, bounded below, for which both raw towers are bounded and retain that band, although their character family is not a Riesz basis. This separates PC-449's empty-resolvent examples from a general obstruction to unbounded densities. It supplies no prime discriminator or RH implication.

## 1. Object and precise claims

Use the singleton base `P_2^*={-1}` and all complete power-map preimages, with coherent lift coordinate `x` in
\[
X=\widehat{\mathbb Z},\qquad \mu=\text{Haar probability}.
\]
At level `m`, retain exactly
\[
(B_m)_{ts}=\begin{cases}
\dfrac{i}{m}\cot\dfrac{\pi(t-s)}m,&t\ne s,\\
0,&t=s,
\end{cases}
\qquad B_m^+=B_m+J_m/m.
\tag{1}
\]
These are the compatible cylinder prescriptions of PC-443, stated explicitly in PC-449. For rational `q` represented in `[0,1)`, their character action is
\[
B\chi_q=b(q)\chi_q,\qquad
b(0)=0,\quad b(q)=1-2q\ (q>0),
\qquad B^+\chi_q=(1-2q)\chi_q.
\tag{2}
\]
Let `nu=w mu` be an equivalent probability: `0<w<infinity` almost everywhere and `integral w dmu=1`. Cylinder functions, equivalently finite linear combinations of characters, are dense in `H_w=L^2(nu)`.

**Spectral rigidity.** If the unchanged augmented cylinder action has a bounded extension to `H_w`, then
\[
\boxed{\sigma(B_w^+)=[-1,1].}
\tag{3}
\]
If additionally `integral w^{-1} dmu<infinity`, boundedness of the unaugmented action is equivalent to boundedness of the augmented action, and its spectrum is also `[-1,1]`. No lower bound on `w` is required for (3).

**Unbounded-density examples.** There exist equivalent probabilities with
\[
0<c\le w,\qquad w\in L^2(\mu),\qquad
\operatorname*{ess\,sup}w=\infty
\tag{4}
\]
for which both unchanged actions extend boundedly, with the spectra just stated. Their norm-one character family is complete but fails even the upper Riesz estimate. Such examples occur arbitrarily close to Haar in total variation.

The weights below are chosen controls, not weights forced by the geometry. The claim concerns the actual weighted operator, not half-density compensation.

## 2. Character modulation recovers interval projections

Suppose `B_w^+` is bounded. Multiplication by any character,
\[
Q_a f=\chi_a f,\qquad a\in\mathbb Q\cap(0,1),
\]
is unitary on `H_w`, regardless of the weight. On `chi_q`, the conjugate `Q_a B_w^+ Q_a^{-1}` has eigenvalue `1-2{q-a}`. The exact sawtooth identity is
\[
a+\frac{(1-2q)-(1-2\{q-a\})}{2}
=\mathbf1_{[0,a)}(q).
\tag{5}
\]
In particular the endpoint `q=0` is included and `q=a` is excluded. Consequently
\[
E_a=aI+\tfrac12(B_w^+-Q_a B_w^+Q_a^{-1})
\tag{6}
\]
is the bounded coordinate projection onto characters in `[0,a)`. All projection and nesting identities follow first on the dense cylinder algebra and then by continuity. With `E_0=0,E_1=I`,
\[
\sup_{a\in[0,1]\cap\mathbb Q}\|E_a\|
\le K:=1+\|B_w^+\|.
\tag{7}
\]
These need not be orthogonal projections. The uniform bound concerns ordered intervals, not arbitrary subsets of the character set.

Fix `z` outside `[-1,1]` and set
\[
g_z(t)=\frac1{1-2t-z},\qquad 0\le t\le1.
\]
For a rational partition `0=a_0<...<a_N=1`, define
\[
R_{z,\mathcal P}=g_z(1)I+
\sum_{j=1}^N\bigl(g_z(a_{j-1})-g_z(a_j)\bigr)E_{a_j}.
\tag{8}
\]
On a character with `a_{k-1}<=q<a_k`, this multiplier is exactly `g_z(a_{k-1})`. Also
\[
\|R_{z,\mathcal P}\|
\le |g_z(1)|+K\int_0^1|g_z'(t)|\,dt
\le \delta^{-1}+2K\delta^{-2},
\qquad \delta=\operatorname{dist}(z,[-1,1]).
\tag{9}
\]
As the partition mesh tends to zero, these operators converge on every cylinder function. The uniform bound (9) extends that convergence strongly to `H_w`, giving a bounded operator `R_z` with `R_z chi_q=g_z(q)chi_q`. Both inverse identities
\[
(B_w^+-z)R_z=R_z(B_w^+-z)=I
\tag{10}
\]
hold on cylinders and hence everywhere. Thus the spectrum is contained in the band. The eigenvalues `1-2q` for rational `q` are dense in the band, proving equality (3). This does not infer an infinite operator's spectrum from finite spectra alone: (6)--(10) construct the missing bounded inverse.

For the unaugmented operator use Haar averaging
\[
Af=\left(\int_X f\,d\mu\right)\mathbf1,
\qquad \|A\|\le\left(\int_X w^{-1}\,d\mu\right)^{1/2}.
\tag{11}
\]
Then `B_w^+=B_w+A`. This proves the boundedness equivalence under the reciprocal-integrability assumption. For `z` off the band,
\[
(B_w-z)^{-1}=R_z+
\left(-\frac1z-\frac1{1-z}\right)A.
\tag{12}
\]
Indeed only the constant character changes eigenvalue, from `1` to `0`. The unaugmented character eigenvalues still have closure `[-1,1]`, proving the second spectral statement.

## 3. Constructing an unbounded density that works

Let `Sx=x+1`. This is invertible and Haar preserving, and is ergodic: on the Haar Fourier basis, its only fixed character is the constant character. Haar probability on `X` is nonatomic.

For nonnegative functions define the uncentered orbit maximal operator
\[
Mf(x)=\sup_{a\le0\le b}
\frac1{b-a+1}\sum_{n=a}^b |f(x+n)|,
\qquad a,b\in\mathbb Z.
\tag{13}
\]
The classical maximal ergodic inequality gives `C=||M||_{L^2(mu)->L^2(mu)}<infinity`: (13) is bounded by the sum of the forward and backward maximal averages. No numerical value of `C` will be used.

Choose a prime `p`, `0<alpha<1/2`, and
\[
h(x)=p^{\alpha v_p(x_p)}.
\tag{14}
\]
Values on the null set `x_p=0` may be assigned arbitrarily. Since
\[
\int_X h^2\,d\mu=(1-p^{-1})
\sum_{j\ge0}p^{(2\alpha-1)j}<\infty,
\]
`h>=1` is in `L^2` and is essentially unbounded. Form the classical Rubio de Francia majorant
\[
W=\sum_{k=0}^{\infty}(2C)^{-k}M^k h,
\qquad w=\frac W{\int_XW\,d\mu}.
\tag{15}
\]
Here `M^0 h=h`. Positivity and the `L^2` maximal bound give
\[
W\ge h\ge1,\qquad \|W\|_2\le2\|h\|_2,
\qquad MW\le2CW.
\tag{16}
\]
The last inequality follows by subadditivity on partial sums and monotone convergence. Thus (4) holds, and `Mw<=2Cw` almost everywhere.

Discarding the union of all integer translates of the null exceptional set makes this inequality valid simultaneously along every remaining orbit. For any finite interval `I` of integer orbit times, its average `a_I` of `w(x+n)` satisfies
\[
a_I\le 2Cw(x+j)\quad(j\in I).
\]
Hence the orbit weight has the uniform discrete `A_2` estimate
\[
\left(\frac1{|I|}\sum_{n\in I}w(x+n)\right)
\left(\frac1{|I|}\sum_{n\in I}\frac1{w(x+n)}\right)
\le2C.
\tag{17}
\]

Theorem 1.2 of Atencia--Martín-Reyes (1983) applies exactly here: for an invertible ergodic transformation of a nonatomic probability space, the uniform orbit `A_2` condition makes the maximal symmetrically truncated ergodic Hilbert transform bounded on `L^2(w mu)`. All its probability, integrability, positivity and ergodicity hypotheses have been checked above.

On cylinders the unaugmented cotangent action is
\[
Bf=\frac1{\pi i}\lim_{N\to\infty}
\sum_{0<|n|\le N}\frac{f(x+n)}n.
\tag{18}
\]
Apply the classical Bernoulli sawtooth Fourier series to each of the finitely many characters in `f` to obtain (2), including `b(0)=0`. The maximal-transform estimate and Fatou's lemma give a uniform weighted norm bound for (18) on the cylinder algebra. It therefore extends boundedly to `H_w`. Since `w` is bounded below, (11) is bounded too; both raw operators now satisfy the spectral theorem proved in Section 2.

The maximal iteration changes the weight throughout the integer orbits. It is not multiplication of PC-449's spike by a bounded factor. PC-449's diverging adjacent-cylinder mass ratios are incompatible with (17), already for two-point intervals.

## 4. What survives and what does not

Every character has norm one in `H_w` and the characters span a dense subspace. If they satisfied an upper Riesz estimate with constant `L`, then for every cylinder function
\[
\int_X |f|^2w\,d\mu\le L\int_X|f|^2\,d\mu.
\tag{19}
\]
Testing cylinder indicators and passing through the generating finite partitions would force `w<=L` almost everywhere, contradicting (4). Thus neither this family nor any enumeration of it is a Riesz basis. Equality of spectral sets has not restored norm equivalence or self-adjointness. PC-444 also rules out symmetry of this unchanged non-Haar action.

For `0<epsilon<=1`, the probability density
\[
w_\epsilon=(1-\epsilon)+\epsilon w
\tag{20}
\]
is still unbounded, bounded below, and satisfies `Mw_epsilon<=2Cw_epsilon`. All preceding conclusions hold for it, while
\[
\|w_\epsilon-1\|_{L^1(\mu)}
=\epsilon\|w-1\|_{L^1(\mu)}\longrightarrow0.
\tag{21}
\]
Together with PC-449, this gives arbitrarily small equivalent perturbations of Haar with two different outcomes: bounded raw towers retaining the band, and closable raw towers whose every closed extension has empty resolvent. Density size or total variation alone does not classify the outcome. Orbit-weight regularity supplies a concrete sufficient condition for the first outcome.

## 5. Prior art, controls and evidence boundary

The weight construction is classical, not a new mechanism. F. J. Martín-Reyes, *Weights for ergodic square functions*, Ann. Inst. H. Poincaré Probab. Statist. **22** (1986), 333--345, [Remark 2.35, p. 345](https://www.numdam.org/item/AIHPB_1986__22_3_333_0.pdf), explicitly gives the iterated-maximal construction of nontrivial ergodic `A_1` weights and points to Rubio de Francia's factorization theory. Equations (15)--(17) prove the exact version used here.

The weighted Hilbert-transform input is E. Atencia and F. J. Martín-Reyes, *The maximal ergodic Hilbert transform with weights*, Pacific J. Math. **108** (1983), 257--263, [Theorem 1.2](https://msp.org/pjm/1983/108-2/pjm-v108-n2-p01-s.pdf). Its conclusion is boundedness of the maximal transform, not the exact spectrum of this cotangent tower.

The interval-projection argument belongs to classical well-bounded operator theory. E. Berkson and T. A. Gillespie, *Spectral decompositions, ergodic averages, and the Hilbert transform*, Studia Math. **144** (2001), 39--61, [DOI 10.4064/sm144-1-2](https://doi.org/10.4064/sm144-1-2), develops spectral families and their relation to ergodic Hilbert transforms. Section 2 above supplies the direct rational-character specialization and inverse construction; no novelty is claimed for bounded-variation spectral calculus.

The local delta is the bounded-action spectral rigidity criterion (3), and its use with the classical weight construction to resolve the unbounded-density boundary left by PC-444 and PC-449. Boundedness of the augmented action cannot create an enlarged or prime-sensitive spectrum, even beyond bounded similarity. Conversely, unbounded density alone does not force PC-449's pathology.

Replace the root-of-unity singleton base by one point at an irrational angle. Every angle difference in (1), the entire character prescription, and the control weights remain identical. The prime `p` in (14) selects a coordinate of an arbitrary control; it does not encode prime birth. This result is control-blind.

**Validation.** Exact rational arithmetic checked (5), including both jump endpoints, in all 87,360 cases with `2<=m<=64`, `a=k/m`, `1<=k<m`, and `q=j/m`. Separate pure-Python complex-arithmetic diagnostics at `m=3,4,8,13,31` compared (6) with direct Fourier interval projections (maximum entry error `4.1e-15`) and checked both inverse formulas at `z=2,i,1/4+i/10` (maximum residual `7.8e-15`). These are finite checks only. The infinite assertions rely on the dense-domain bounded-inverse argument and the stated external weighted-transform theorem.

**Limits and decisive audit.** No necessity of orbit `A_2` for the bounded *nonmaximal* raw action is asserted. Arbitrary nonclosable measures, unbounded raw realizations, multi-point base towers, and changes of kernel are not classified. The argument must preserve the augmented endpoint in (5), reciprocal integrability where (11) is used, a uniform bound before passing from cylinders to the whole space, and the orbit rather than merely global weight condition (17). A bounded augmented realization with an off-band spectral point would falsify (3); an upper Riesz estimate for the constructed character family would falsify (19)'s consequence. No RH implication or new source-forced coupling is established.
