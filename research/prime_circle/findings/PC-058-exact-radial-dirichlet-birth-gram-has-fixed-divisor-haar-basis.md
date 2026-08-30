# PC-058 — exact radial Dirichlet birth Gram has a fixed divisor-Haar basis

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the exact finite-radius Dirichlet Gram family on finite divisor boxes. The entire kernel class

\[
K_F(m,n)=\gcd(m,n)F(\operatorname{lcm}(m,n))
\]

is simultaneously diagonalizable after Möbius birth extraction and the canonical `phi` shell normalization. The eigenbasis is independent of the scalar function `F`: it is an explicit tensor product of prime-power divisor-Haar vectors. In particular, the exact prime-circle radial family

\[
F_x(L)=-\log(1-x^L),\qquad 0<x<1,
\]

shares one fixed basis for every radius. Radius changes only eigenvalues; it never mixes prime/divisor modes. This strictly strengthens the boundary classification in PC-056/PC-057: the leading GCD collision form, the finite resultant/discriminant term, every higher boundary jet, and the unexpanded finite-radius Gram matrix all live in the same commuting finite-dimensional algebra.

This does **not** classify arbitrary two-dimensional operators, non-divisor-closed exhaustions, nonlinear entrywise deformations, or infinite-volume operator domains. It rules out extracting a new Hilbert–Pólya mechanism merely by retaining more radial orders, combining several radii through ordinary operator functional calculus, or hoping that the exact finite-radius Dirichlet birth Gram develops noncommuting cross-prime spectral flow hidden by the first two boundary terms.

## 1. Exact Dirichlet kernel before taking the boundary limit

For the full-root logarithmic fields

\[
V_n(z)=\Log(1-z^n),
\qquad V_{n,r}(z)=V_n(rz),
\qquad x=r^2,
\]

PC-006/PC-056 give the exact analytic Dirichlet Gram matrix

\[
\boxed{
G^{\rm full}_{m,n}(x)
=-\gcd(m,n)\log\!\left(1-x^{\operatorname{lcm}(m,n)}\right).
}
\]

Thus for each fixed `x` this is a member of the broader family

\[
\boxed{
K_F(m,n)=\gcd(m,n)F(\operatorname{lcm}(m,n)),
}
\]

with

\[
F=F_x,
\qquad
F_x(L)=-\log(1-x^L).
\]

Let `N` be fixed and restrict shell indices to the full divisor box

\[
\mathcal D(N)=\{d:d\mid N\}.
\]

Let

\[
M(n,d)=\mu(n/d)\mathbf 1_{d\mid n}
\]

be the divisor Möbius matrix and

\[
D_\varphi=\operatorname{diag}(\varphi(d))_{d\mid N}.
\]

Primitive/birth extraction and shell normalization give

\[
\boxed{
Q_F=M K_F M^{\mathsf T},
\qquad
S_F=D_\varphi^{-1/2}Q_FD_\varphi^{-1/2}.
}
\]

The question left open by PC-057 is whether keeping the **entire** function `F_x`, rather than only its leading and finite boundary terms, creates new eigenvectors or noncommuting radial dynamics. It does not.

## 2. Prime-power chain: all functions share the same generalized eigenvectors

First take one prime power box

\[
\mathcal D(p^A)=\{1,p,\ldots,p^A\}
\]

and write exponents as `a=0,...,A`. Put

\[
f_a=F(p^a).
\]

Then

\[
\boxed{
(K_f)_{a,b}=p^{\min(a,b)}f_{\max(a,b)}.
}
\]

On this chain the Möbius matrix is simply the first-difference matrix

\[
(M_p)_{a,b}
=
\begin{cases}
1,&a=b,\\
-1,&a=b+1,\\
0,&\text{otherwise},
\end{cases}
\]

and

\[
D_p=\operatorname{diag}(\varphi(p^a))_{a=0}^A.
\]

Define one constant vector

\[
\boxed{
v_{p,*}=(1,1,\ldots,1)^{\mathsf T}
}
\]

and, for every `j=0,...,A-1`, the local divisor-Haar vector

\[
\boxed{
(v_{p,j})_a=
\begin{cases}
1-p,&0\le a\le j,\\
1,&a=j+1,\\
0,&a>j+1.
\end{cases}
}
\]

These vectors are independent of `f`. Their decisive property is visible before any matrix multiplication:

\[
\boxed{
M_p^{\mathsf T}v_{p,*}=e_A,
\qquad
M_p^{\mathsf T}v_{p,j}=-p e_j+e_{j+1}.
}
\]

For the constant vector, the last column of `K_f` is

\[
(K_f e_A)_a=p^a f_A,
\]

so one further first difference gives

\[
\boxed{
M_pK_fM_p^{\mathsf T}v_{p,*}
=f_A D_pv_{p,*}.
}
\]

For `v_{p,j}`, put

\[
c_j=p f_j-f_{j+1}.
\]

Then

\[
K_f(-p e_j+e_{j+1})
=(-c_j,-c_jp,\ldots,-c_jp^j,0,\ldots,0)^{\mathsf T},
\]

and applying `M_p` gives exactly

\[
\boxed{
M_pK_fM_p^{\mathsf T}v_{p,j}
=rac{p f_j-f_{j+1}}{p-1}D_pv_{p,j}.
}
\]

Therefore the complete generalized spectrum of `(Q_f,D_p)` is

\[
\boxed{
\lambda_{p,*}(f)=f_A,
\qquad
\lambda_{p,j}(f)=\frac{p f_j-f_{j+1}}{p-1},
\quad 0\le j<A.
}
\]

The basis is also exactly `D_p`-orthogonal:

\[
v_{p,*}^{\mathsf T}D_pv_{p,*}=p^A,
\]

\[
v_{p,j}^{\mathsf T}D_pv_{p,k}=0
\quad(j\ne k),
\]

\[
\boxed{
v_{p,j}^{\mathsf T}D_pv_{p,j}=(p-1)p^{j+1}.}
\]

Hence the ordinary normalized matrices

\[
S_f=D_p^{-1/2}Q_fD_p^{-1/2}
\]

all have the same orthogonal eigenvectors `D_p^{1/2}v_{p,*}` and `D_p^{1/2}v_{p,j}`, regardless of the function `f`.

## 3. Full divisor boxes inherit a tensor-product common basis

Write

\[
N=\prod_{p\mid N}p^{A_p}
\]

and identify a divisor with its valuation tuple

\[
d\longleftrightarrow(a_p)_{p\mid N},
\qquad 0\le a_p\le A_p.
\]

In valuation order,

\[
\boxed{
M_N=\bigotimes_{p\mid N}M_p,
\qquad
D_\varphi=\bigotimes_{p\mid N}D_p.
}
\]

If a function on the divisor box is a pure tensor,

\[
F\!\left(\prod_p p^{a_p}\right)=\prod_p f_p(a_p),
\]

then meet/join factorization of the divisor lattice gives

\[
\boxed{
K_F=\bigotimes_{p\mid N}K_{f_p}.
}
\]

Every function on the finite valuation grid is a linear combination of pure tensors. Since the local eigenvectors above do **not** depend on the local function, linearity implies that the tensor basis

\[
\boxed{
v_{\boldsymbol\alpha}
=\bigotimes_{p\mid N}v_{p,\alpha_p},
\qquad
\alpha_p\in\{*,0,\ldots,A_p-1\},
}
\]

diagonalizes `Q_F` relative to `D_phi` for **every** scalar function `F` on `D(N)`.

Equivalently, define local linear functionals on the valuation coordinate by

\[
\ell_{p,*}(f)=f(A_p),
\]

\[
\boxed{
\ell_{p,j}(f)=\frac{p f(j)-f(j+1)}{p-1}.
}
\]

For an arbitrary, not necessarily multiplicative, divisor function `F`, the eigenvalue of mode `boldsymbol alpha` is the mixed finite-difference functional

\[
\boxed{
\lambda_{\boldsymbol\alpha}(F)
=\left(\bigotimes_{p\mid N}\ell_{p,\alpha_p}\right)F.
}
\]

Consequently the normalized family is a commuting algebra:

\[
\boxed{
S_F S_G=S_G S_F
\qquad\text{for all }F,G:\mathcal D(N)\to\mathbb C.
}
\]

In the unnormalized birth coordinates the equivalent statement is

\[
\boxed{
Q_FD_\varphi^{-1}Q_G
=Q_GD_\varphi^{-1}Q_F.
}
\]

This is stronger than the prime-separable first-boundary spectrum in PC-057. An arbitrary `F(lcm)` can couple several primes numerically in its eigenvalues, but it cannot create **cross-prime eigenvector mixing or noncommuting spectral dynamics**.

## 4. Exact radial prime-circle Gram matrices commute at every radius

Apply the theorem to

\[
F_x(d)=-\log(1-x^d),
\qquad 0<x<1.
\]

For every pair of physical radii `x,y` and every finite divisor box,

\[
\boxed{
S_xS_y=S_yS_x,
}
\]

and the common eigenvectors depend only on the prime-power exponents in `N`, not on `x`.

On a single prime-power chain the exact eigenvalues are already elementary:

\[
\boxed{
\lambda_{p,*}(x)
=-\log(1-x^{p^A}),
}
\]

and

\[
\boxed{
\lambda_{p,j}(x)
=
\frac{-p\log(1-x^{p^j})+\log(1-x^{p^{j+1}})}{p-1}.
}
\]

For general `N`, the eigenvalues are finite mixed differences of the same logarithms. Thus each mode has the form

\[
\boxed{
\lambda_{\boldsymbol\alpha}(x)
=\sum_{d\mid N}c_{\boldsymbol\alpha}(d)
\bigl[-\log(1-x^d)\bigr],
\qquad c_{\boldsymbol\alpha}(d)\in\mathbb Q.
}
\]

After clearing denominators by an integer `q`, exponentiation gives a finite rational cyclotomic product

\[
\boxed{
\exp\!\bigl(q\lambda_{\boldsymbol\alpha}(x)\bigr)
=\prod_{d\mid N}(1-x^d)^{-q c_{\boldsymbol\alpha}(d)}.
}
\]

So the exact finite-box radial eigenmodes have only the finite roots-of-unity divisor inherited from the factors `1-x^d`; no hidden zeta divisor is created by diagonalization.

Moreover `K_{F_x}` is the genuine Dirichlet Gram matrix of the linearly independent full-root fields, and `M` is invertible. Therefore

\[
\boxed{
S_x>0\qquad(0<x<1),
}
\]

so none of the exact physical radial eigenvalues crosses zero. A complex continuation in `x` can of course be manufactured, but its mode functions remain finite logarithmic/cyclotomic combinations on each divisor box.

## 5. PC-056 and PC-057 are the first two coefficients of the same fixed-basis family

Put

\[
x=e^{-t},
\qquad t\to0^+.
\]

For `y=Lt`,

\[
-\log(1-e^{-y})
=-\log y+\frac y2
-\sum_{k\ge1}
\frac{B_{2k}}{2k(2k)!}y^{2k}.
\]

Define the power-GCD family already used in PC-057,

\[
H_\tau(m,n)
=\gcd(m,n)\operatorname{lcm}(m,n)^{-\tau}.
\]

Then the **whole boundary jet** of the exact Gram family is

\[
\boxed{
G^{\rm full}(e^{-t})
=(-\log t)H_0+H'_0
+\frac t2H_{-1}
-\sum_{k\ge1}
\frac{B_{2k}}{2k(2k)!}t^{2k}H_{-2k}.
}
\]

Thus PC-056 is the normalized `H_0` term and PC-057 is `H'_0`. Every higher coefficient is another member of the same simultaneously diagonalized algebra.

For `F_\tau(d)=d^{-\tau}`, the local eigenvalues specialize to

\[
\boxed{
\lambda_{p,*}(\tau)=p^{-A_p\tau},
}
\]

\[
\boxed{
\lambda_{p,j}(\tau)
=p^{-j\tau}
\frac{p-p^{-\tau}}{p-1}.
}
\]

Because `F_tau` is multiplicative, the global eigenvalues are products of these prime-local factors. At `tau=0` every eigenvalue is `1`, recovering the Smith identity

\[
D_\varphi^{-1/2}MH_0M^{\mathsf T}D_\varphi^{-1/2}=I.
\]

Differentiating the fixed-basis eigenvalues at `tau=0` gives

\[
(\log p)(-A_p)
\]

for the `*` mode and

\[
\boxed{
(\log p)\left(\frac1{p-1}-j\right)
}
\]

for mode `j`, exactly the prime-local spectrum derived independently in PC-057. This provides a direct audit check on both findings and shows that the apparent Kronecker-sum structure of the finite boundary term is simply the tangent at the identity of a fixed tensor-product diagonal family.

## 6. Why retaining more radial information does not create an RH mechanism

PC-057 left open the possibility that the first two boundary terms were misleadingly simple while the exact two-dimensional radial Gram family might develop a genuinely collective spectrum. The simultaneous-diagonalization theorem rules out that specific escape.

On every finite divisor box:

\[
\boxed{
\text{exact radial Dirichlet Gram}
\longrightarrow
\text{Möbius birth extraction}
\longrightarrow
\text{fixed divisor-Haar basis}
\longrightarrow
\text{commuting scalar radial modes}.
}
\]

No avoided crossings, changing eigenspaces, noncommuting transport, Berry-type curvature, or cross-prime eigenvector dynamics can arise from varying the radius inside this kernel class. Any finite sum, product, polynomial, resolvent, or ordinary joint functional calculus built from several `S_x` or boundary-jet matrices stays diagonal in the same basis.

This does not prevent one from appending a Mellin/Dirichlet transform to the scalar eigenvalue functions, taking an infinite-volume limit, or analytically continuing them. But those operations are additional structures. At finite divisor level the exact radial geometry has already reduced to explicit divisor-lattice finite differences of `log(1-x^d)`, and it supplies neither a functional-equation involution nor a critical-line spectral condition.

## 7. Prior-art and novelty audit

The ambient matrix theory is classical and broad enough that no historical novelty should be claimed for the abstract appearance of meet/join incidence algebra.

Mika Mattila, **On the eigenvalues of combined meet and join matrices**, *Linear Algebra and its Applications* **466** (2015), 1–20, DOI `10.1016/j.laa.2014.10.001`, treats common generalizations of meet and join matrices, including GCD/LCM specializations, via lattice incidence factorizations and eigenvalue analysis. Pauliina Ilmonen and Vesa Kaarnioja, **Generalized eigenvalue problems for meet and join matrices on semilattices**, *Linear Algebra and its Applications* **536** (2018), 250–273, DOI `10.1016/j.laa.2017.09.023`, explicitly study generalized eigenvalue problems for meet/join matrices and sharpen them on the divisor lattice. These are direct prior-art boundaries for treating the generalized pair `(Q_F,D_phi)` as a novel spectral formalism.

For squarefree divisor boxes, Titus Hilberdink, **The group of squarefree integers**, *Linear Algebra and its Applications* **457** (2014), 383–399, DOI `10.1016/j.laa.2014.05.037`, develops the finite divisor group under the lcm/gcd operation, its characters, associated arithmetic-matrix factorizations, and explicit eigenvalues. This independently shows that fixed product/character diagonalization in the Boolean divisor case is classical territory.

Directed searches did not locate the exact statement that the specific Möbius-normalized family

\[
\gcd(m,n)F(\operatorname{lcm}(m,n))
\]

for arbitrary `F` on a full nonsquarefree divisor box has the explicit local vectors `v_{p,*},v_{p,j}` above, nor the application to the full finite-radius prime-circle Dirichlet Gram family. Absence of an exact wording is **not** a novelty claim. The durable Mathia contribution is the project-specific closure: once the exact radial harmonic kernel is recognized as a meet/join divisor-lattice family, all radii and all boundary orders share one explicit basis, so the apparent remaining radial spectral freedom after PC-057 disappears.

## 8. Boundaries and exact falsification tests

The obstruction is deliberately finite and structural. It does **not** rule out:

- a different intrinsic two-dimensional operator whose shell kernel is not of the form `gcd(m,n) F(lcm(m,n))`;
- non-divisor-closed truncations with a separate geometric justification and a demonstrably different limit;
- an infinite completion in which domains, renormalization, or loss of boundedness introduces new operator theory beyond the finite common basis;
- entrywise nonlinear transformations that are not ordinary functions/compositions of the commuting operators;
- nonlinear dynamics coupling the actual fields before forming a Gram matrix;
- the Fuchsian uniformization/accessory-parameter branch of PC-017.

It **does** rule out claiming that more radial resolution within the exact Dirichlet Gram family itself supplies the missing noncommutative or critical-line mechanism.

The theorem can be falsified by finite exact checks:

1. on `D(p^A)`, verify `M_p^T v_* = e_A` and `M_p^T v_j=-p e_j+e_{j+1}`;
2. multiply by `K_f` for symbolic independent values `f_0,...,f_A` and recover the displayed generalized eigenvalues;
3. verify `D_p`-orthogonality and completeness of the `A+1` local vectors;
4. tensor the construction on arbitrary `N` and verify `Q_F D_phi^{-1} Q_G = Q_G D_phi^{-1} Q_F` for arbitrary independent tables `F,G` on `D(N)`;
5. substitute `F_x(d)=-log(1-x^d)` and compare the resulting eigenvalues with direct numerical diagonalization at several radii;
6. differentiate the power-GCD eigenvalues at `tau=0` and recover exactly the local spectrum of PC-057.

A failure of any one of these exact finite identities invalidates the common-basis claim. An infinite-dimensional escape must explain precisely what survives the divisor-box common diagonalization and why that added structure is intrinsic to prime-circle geometry rather than an externally chosen completion.