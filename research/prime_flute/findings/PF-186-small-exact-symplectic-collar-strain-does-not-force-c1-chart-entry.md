# PF-186 — small exact-symplectic collar strain does not force entry into a fixed `C^1` generating chart

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE/BOUNDARY + CLASSICAL-CONSTRUCTION`. PF-185 removes the linearized/Killing-field obstruction on the normalized short-collar slab and proves the desired energy-local exact-area cutoff once the canonical relative germ lies in one fixed `C^1` generating neighborhood of the identity. That chart-entry hypothesis cannot be obtained from small metric strain, exact symplecticity, zero annular flux, and the zero-twist reflection alone. On the same fixed normalized slab there are reflection-equivariant compactly supported Hamiltonian diffeomorphisms whose source- and inverse-side metric deviation tends to zero even in `L^infinity`, whose displacement tends uniformly to zero, and whose annular flux is exactly zero, but whose derivative equals `-I` at two reflected points. They therefore stay a fixed positive distance from the identity in `C^1`. The obstruction is a localized nonlinear rotation carried on exponentially separated radial scales; it is invisible to strain because rotations are local isometries and the change of rotation angle can be made arbitrarily slow in logarithmic radius. Thus the remaining PF-183/PF-185 splice problem cannot be closed by a generic theorem of the form “small local strain + marking + exactness implies `C^1` chart entry.” A positive proof must exploit additional structure of the **canonical PF-179--PF-184 relative germs** or localize exact symplectically at Sobolev regularity without first entering a fixed `C^1` graph chart. This finding does not prove that the canonical prime/shift germ contains such microtwists and does not disprove the desired `S_r`, `r>1`, splice estimate.

## Claim

Let

\[
A=[1,5/4]\times \mathbb R/\mathbb Z,
\qquad
g_L=\frac{dx^2}{L^2+x^2}+(L^2+x^2)d\theta^2,
\qquad 0\le L\le \mu_*,
\]

with area form `dx wedge dtheta`, and let

\[
R(x,\theta)=(x,-\theta)
\]

be the PF-142/PF-185 reflection. For every `1<r<infinity` there are smooth diffeomorphisms

\[
H_j:A\to A
\]

(with the construction uniform in `L`) such that:

1. `H_j` is the identity near both boundary circles;
2. `H_j` preserves `dx wedge dtheta` and is Hamiltonian, hence its annular action/flux class is zero;
3. `H_j R=R H_j`;
4. for the Güneysu--Thalmaier multiplicative metric deviation used in PF-175,
   \[
   \|\delta_{g_L,H_j^*g_L}\|_{L^\infty(A)}
   +\|\delta_{g_L,(H_j^{-1})^*g_L}\|_{L^\infty(A)}\longrightarrow0;
   \]
   in particular both corresponding `L^r` energies tend to zero;
5. `\|H_j-id\|_{C^0}\to0`, but
   \[
   \boxed{\|DH_j-I\|_{L^\infty}\ge2}
   \]
   for every `j`.

Consequently there is no fixed `C^1` neighborhood of the identity whose membership follows only from vanishing local metric strain together with exact symplecticity, reflection marking, zero flux, and boundary identity. The same counterexample already occurs with `L^+=L` (`t=0`), so allowing the small PF-183 collar-length mismatch cannot repair that implication.

## 1. A logarithmically slow Hamiltonian half-turn

Fix an interior point

\[
z_+=(x_0,\theta_0),\qquad 1<x_0<5/4,
\]

with `theta_0` away from the reflection fixed set, and put `z_-=Rz_+`. Choose the supports below so small that the two reflected disks are disjoint and avoid the boundary of `A`.

Write `a_0=L^2+x_0^2`. In a neighborhood of `z_+` use the linear area-preserving coordinate

\[
(x,\theta)=z_+ + B_L y,
\qquad
B_L=\operatorname{diag}(\sqrt{a_0},a_0^{-1/2}).
\]

Because `det B_L=1`, the area form is still `dy_1 wedge dy_2`; moreover

\[
B_L^T g_L(z_+)B_L=I.
\]

The matrices `B_L` and `B_L^{-1}` are uniformly bounded for `0<=L<=mu_*` because `x_0` stays in the fixed thick slab.

Choose `rho_j->0` and `m_j->infinity`, and put

\[
a_j=\rho_j e^{-m_j}.
\]

Let `chi` be a fixed smooth cutoff equal to one near `(-infinity,0]`, zero near `[1,infinity)`, and flat at the endpoints. Define a smooth radial angle by

\[
\alpha_j(s)=
\begin{cases}
\pi,&0\le s\le a_j,\\
\pi\,\chi\!\left(\dfrac{\log(s/a_j)}{m_j}\right),&a_j<s<\rho_j,\\
0,&s\ge\rho_j.
\end{cases}
\]

Then

\[
\boxed{\sup_s |s\alpha_j'(s)|\le \frac{C}{m_j}\to0.}
\]

In polar coordinates `y=(s,phi)`, set

\[
T_j(s,\phi)=(s,\phi+\alpha_j(s)).
\]

This is a smooth compactly supported Hamiltonian diffeomorphism: for the standard area form `s ds wedge dphi`, choose a radial Hamiltonian with `h_j'(s)=s\alpha_j(s)` (up to the harmless sign convention). Its time-one map is `T_j`.

On the inner disk `s<=a_j`, `T_j(y)=-y`; hence

\[
DT_j(0)=-I.
\]

The total rotation is order one, but it is accumulated across a logarithmic radial interval of length `m_j`, so its non-isometric shear tends to zero.

## 2. The metric strain tends uniformly to zero

In the orthonormal polar frames of the frozen Euclidean metric, the derivative of the twist has the form

\[
DT_j=Q_{\alpha_j}
\begin{pmatrix}1&0\\ s\alpha_j'(s)&1\end{pmatrix},
\]

where `Q_alpha` is a rotation. Thus the frozen-metric strain sees only the shear:

\[
(DT_j)^TDT_j-I=O(m_j^{-1}).
\]

Let

\[
G_{L,j}(y)=B_L^T g_L(z_+ + B_Ly)B_L.
\]

The family `g_L`, `0<=L<=mu_*`, is uniformly `C^1` on the fixed slab, so

\[
G_{L,j}(y)=I+O(\rho_j)
\]

uniformly on the support. Since the twist preserves `|y|`, both the source and image stay in that same shrinking neighborhood. Combining the previous two estimates gives

\[
(DT_j)^T G_{L,j}(T_jy)DT_j-G_{L,j}(y)
=O(m_j^{-1}+\rho_j)
\]

uniformly in `L`.

The relative metric eigenvalues therefore equal `1+O(m_j^{-1}+rho_j)`, and the multiplicative deviation used by PF-175 obeys

\[
\boxed{
\|\delta_{g_L,T_j^*g_L}\|_\infty
\le C(m_j^{-1}+\rho_j).
}
\]

The inverse is the same twist with angle `-alpha_j`, so it satisfies the identical bound. Because the support has area `O(rho_j^2)`, the `L^r` energies tend to zero a fortiori for every finite `r`; indeed the stronger `L^infinity` strain already tends to zero.

## 3. Reflection marking and zero flux do not remove the microtwist

Transport `T_j` to the disk around `z_+` using the area coordinate above. On the reflected disk define the conjugate map

\[
T_j^-:=R\,T_j^+\,R,
\]

and set the map equal to the identity elsewhere. The supports are disjoint and each local map is already the identity near its support boundary, so this gives one smooth global diffeomorphism `H_j`.

Because `R` is an isometry and anti-symplectic, the double conjugation preserves symplecticity, and the paired construction satisfies

\[
H_jR=RH_j.
\]

Each disk twist is Hamiltonian and compactly supported away from the annulus boundary. Their disjoint union is therefore Hamiltonian as well. In particular

\[
H_j^*(x\,d\theta)-x\,d\theta=dS_j
\]

for a globally defined primitive after the usual choice of additive constant, so the annular period/flux is exactly zero. The map also fixes a neighborhood of both boundary circles and the reflection fixed axes.

Thus this construction survives precisely the topological and marking gates supplied by PF-142 and PF-184.

## 4. Why it never enters the PF-185 `C^1` chart

At the centers of both disks the map fixes the point and performs a half-turn, so

\[
DH_j(z_+)=DH_j(z_-)=-I.
\]

Hence

\[
\|DH_j-I\|_\infty\ge2
\]

for all `j`, even though the metric strain and the `C^0` displacement tend to zero. In the standard local graph picture around the diagonal, the same half-turn is exactly the loss of transversality one expects: at the fixed center the tangent to the graph is `(v,-v)`, whose projection to the diagonal by the sum direction vanishes. The near-identity generating-function argument used in PF-185 therefore cannot be entered merely by shrinking the strain.

This does not contradict PF-185's marked Korn estimate. Korn controls an **infinitesimal displacement field** modulo Killing fields, and PF-185's nonlinear absorption starts only after `H=id+u` is already in a fixed `C^1` neighborhood. Here the nonlinear derivative stays on the rotation group while the selected rotation changes across many logarithmic scales. The set on which the derivative is far from `I` becomes tiny, so Sobolev geometric-rigidity estimates remain compatible with the example.

## 5. Adversarial checks and boundary of the negative result

The example is stronger than an `L^r` concentration counterexample in one respect: its **pointwise metric distortion tends to zero**. The failure is therefore not caused by hiding a large strain spike on a small set. What is hidden is an order-one rotation, which strain cannot see locally.

Several stronger conclusions do **not** follow:

- the example does not show that the canonical PF-179--PF-184 relative germ actually contains a microtwist;
- it does not show that an energy-local exact symplectic splice satisfying PF-183(11) is impossible;
- it does not refute a low-regularity generating-function/localization theorem that avoids `C^1` graph entry;
- it does not address the `r=1` trace endpoint.

The decisive implication it does refute is narrower and exact:

\[
\boxed{
\text{small strain + exactness + reflection + zero flux}
\not\Longrightarrow
\text{fixed `C^1` near-identity chart entry}.
}
\]

Therefore any proof of the PF-183 splice estimate that uses PF-185's near-identity generating chart must obtain chart entry from **additional canonical structure** of the assembled prime/shift body germ, not from its energy budget alone.

## Prior art and novelty assessment

No novelty is claimed for radial Hamiltonian twists, compactly supported Hamiltonian diffeomorphisms, Korn/geometric rigidity, or quasiconformal near-isometry phenomena. Friesecke--James--Müller control the `L^2` distance of a gradient from one rotation by nonlinear strain; Conti--Dolzmann--Müller give the corresponding `L^p`/mixed-growth rigidity framework used near PF-185; standard symplectic topology supplies compactly supported Hamiltonian isotopies. A targeted audit also found the boundary-fixed quasiconformal displacement literature (for example Vuorinen--Zhang, *Distortion of quasiconformal mappings with identity boundary values*, JLMS 2014, DOI `10.1112/jlms/jdu043`), which is consistent with the construction: small dilatation plus fixed boundary controls displacement, not a pointwise choice of derivative frame.

The project-specific durable content is the explicit placement of this classical flexibility inside the **normalized PF-185 short-collar model with exact area, zero annular flux, and the PF-142 reflection marking simultaneously imposed**. It closes one tempting shortcut in the PF-183/PF-185 route. The literature audit does not support a novelty claim for the underlying twist mechanism.

## Consequences for the research line

PF-184 and PF-185 still remove genuine obstructions: flux and the linearized Killing kernel are gone. PF-186 shows that they do not by themselves select a nonlinear derivative branch near the identity. The live `S_r`, `r>1`, route now has two honest options: derive `C^1` chart entry from the explicit canonical PF-179--PF-184 construction (using more than metric energy), or prove an exact-area localization estimate directly at Sobolev/energy regularity that is stable under localized rotations of the kind above. Any argument that silently upgrades `L^r` or even `L^infinity` metric strain to `C^1` closeness without such extra input is invalid.